from django.test import TestCase
from model_bakery import baker
from rest_framework.test import APIClient ,APIRequestFactory
from Usuarios.models import User 
from datetime import date
from .models import Categoria, Evento  
from Eventos.views import EventoView

class EventoViewTestCase(TestCase):
    def setUp(self):

        self.categoria = baker.make(Categoria)
        self.user = baker.make(User)  
        self.user2 = baker.make(User)
        self.evento_com_user = baker.make(
            Evento,
            user=self.user,
            data=date.today(),
            descricao="Descrição do evento com usuário",
            valor_entrada=10.00,
            categoria=self.categoria,
        )

        # Crie outro evento não associado a nenhum usuário
        self.evento_sem_user = baker.make(
            Evento,
            user=None,
            data=date.today(),
            descricao="Descrição do evento sem usuário",
        )

        self.evento_user2 = baker.make(
            Evento,
            user=self.user2,
            data=date.today(),
            descricao="Descrição do evento usuário2",
        )

    def test_get_events_by_user(self):
        factory = APIRequestFactory()
        request = factory.get('/user/eventos/')
        request.query_params = {"user_id": self.user.id}
        response = EventoView().get_events_by_user(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

 