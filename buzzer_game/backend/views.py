from django.shortcuts import render
import json
import time
from django.http import StreamingHttpResponse
# Create your views here.

from .models import Team, Player, Question
from .serializers import TeamSerializer, PlayerSerializer, QuestionSerializer
from rest_framework import viewsets
from .sse_state import SSSEState, State
from dataclasses import asdict


def index_view(request):
    return render(request, "index.html")


def sse_view(request):
    # Ensure the connection is a live one

    # Generator for the streaming response
    def event_stream():
        for i in range(1, 101):  # Example: Send 10 updates
            data = SSSEState(State.ANSWER_CORRECT.value, active_team_id=i)
            yield f"data: {json.dumps(asdict(data))}\n\n"  # SSE format
            time.sleep(0.5)  # Simulate delay between updates

    # Streaming response with proper content type
    return StreamingHttpResponse(event_stream(), content_type="text/event-stream")


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
