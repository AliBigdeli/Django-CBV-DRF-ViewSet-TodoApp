from rest_framework.routers import DefaultRouter
from .views import TodoListView, TodoDetailApiView

router = DefaultRouter()
router.register("task-list", TodoListView, basename="task_list")
router.register(
    "task-detail",
    TodoDetailApiView,
    basename="task_detail",
)

urlpatterns = []

urlpatterns += router.urls
