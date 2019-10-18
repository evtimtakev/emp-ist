from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project, Employee


class ProjectView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        all_projects_full = []
        for p in Project.objects.all():
            employees_for_project = [{"name": e.name, "email": e.email} for e in p.employees.all()]
            all_projects_full.append({
                "name": p.title,
                "client": p.client.name,
                "employees": employees_for_project
            })

        return Response(all_projects_full)
