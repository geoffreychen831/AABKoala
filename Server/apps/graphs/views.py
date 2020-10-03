import os

from django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions, mixins, status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
import json

from apps.graphs import models
from apps.graphs.models import Result, Graph, Reading
from apps.graphs.serializers import ResultSerializer, UserSerializer, GraphSerializer
from utils import plot


class ResultViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ResultListViewSet(APIView):
    serializer_class = ResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = ResultSerializer(data=request.data, many=True)
        else:
            serializer = ResultSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GraphViewSet(APIView):
    def get(self, request):
        graphs = Graph.objects.all()
        serializer = GraphSerializer(graphs, many=True)
        return Response(serializer.data)

    def post(self, request):
        graphType = json.loads(request.body.decode('utf-8')).get('graphType')
        if graphType == "NDS_3DCRT":
            return plot_NDS_3DCRT(self, request)

    def delete(self, request):
        graphs_list = json.loads(request.body.decode('utf-8')).get('graphs_list')

        graphs_obj = Graph.objects.filter(pk__in=graphs_list)
        for graph_obj in graphs_obj:
            url = graph_obj.url
            os.remove(url)
            graph_obj.result.clear()
            graph_obj.delete()

        return Response(status=status.HTTP_200_OK)


def plot_NDS_3DCRT(self, request):
    results_list = json.loads(request.body.decode('utf-8')).get('results_list')
    mode = json.loads(request.body.decode('utf-8')).get('mode')
    series_name = []
    for resultID in results_list:
        current_results = Result.objects.filter(id=resultID)
        for current_result in current_results:
            series_name.append(current_result.FacilityName)
    print("Series name:")
    print(series_name)
    readings = Reading.objects.filter(result_id__in=results_list)
    data = {"101106": [], "110106": [], "205106": [], "208106": [], "205206": [], "208206": [], "205306": [],
            "208306": [], "303106": [], "305106": [], "403106": [], "405106": [], "103110": [], "110110": [],
            "303110": [], "305110": [], "403110": [], "405110": [], "103115": [], "110115": [], "303115": [],
            "305115": [], "403115": [], "405115": [], "103118": [], "110118": [], "303118": [], "305118": [],
            "403118": [], "405118": [], "101105": [], "110105": [], "303105": [], "305105": [], "103109": [],
            "110109": [], "303109": [], "305109": []}

    for reading in readings:
        for key in data.keys():
            temp = "data[key].append(reading.Reading_" + key + ")"
            exec(temp)

    # If mode is history, load history readings from the DB
    if mode == "history":
        # Load all history readings
        history_readings = Reading.objects.all()

        history_data = {"101106": [], "110106": [], "205106": [], "208106": [], "205206": [], "208206": [],
                        "205306": [],
                        "208306": [], "303106": [], "305106": [], "403106": [], "405106": [], "103110": [],
                        "110110": [],
                        "303110": [], "305110": [], "403110": [], "405110": [], "103115": [], "110115": [],
                        "303115": [],
                        "305115": [], "403115": [], "405115": [], "103118": [], "110118": [], "303118": [],
                        "305118": [],
                        "403118": [], "405118": [], "101105": [], "110105": [], "303105": [], "305105": [],
                        "103109": [],
                        "110109": [], "303109": [], "305109": []}
        for history_reading in history_readings:
            for history_key in history_data.keys():
                tmp = "history_data[history_key].append(history_reading.Reading_" + history_key + ")"
                exec(tmp)
        # Plot with history data
        data_list = [history_data, data]
        graph_info = plot.NDS_3DCRT(data_list, series_name, mode)
    else:
        # Plot without history data
        data_list = [data]
        graph_info = plot.NDS_3DCRT(data_list, series_name, mode)

    graph_obj = models.Graph.objects.create(url=graph_info['url'], fileName=graph_info['fileName'])
    results_obj = models.Result.objects.filter(pk__in=results_list)
    graph_obj.result.add(*results_obj)
    graph_obj.save()
    return Response(graph_info, status=status.HTTP_200_OK)
