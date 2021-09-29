from rest_framework.response import Response
from todo.models import Task
from .serializers import TaskSerializer
from rest_framework import permissions
from rest_framework import viewsets


class TodoListView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(user=self.request.user)
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoDetailApiView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "todo_id"

    def get_object(self, queryset=None):
        obj = Task.objects.get(pk=self.kwargs["todo_id"])
        return obj

    def delete(self, request, *args, **kwargs):
        object = self.get_object()
        object.delete()
        return Response({"detail": "successfully removed"})

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        object = self.get_object()
        serializer = TaskSerializer(
            data=request.data, instance=object, many=False
        )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
