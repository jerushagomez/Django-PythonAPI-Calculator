# Create your views here.

from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from report.mixins import APILoggingMixin
from .serializer import CalcSerializer
from .utils import calculator


@api_view(['GET'])
@permission_classes([])
def api_root(request, format=None):
    return Response({
        'StandardCalculator': reverse('standard-calculator', request=request, format=format),
    })


class StandardCalculator(APILoggingMixin, APIView):

    permission_classes = [permissions.AllowAny]
    api_name = 'StandardCalculator'
    def get(self, request):
        data = request.query_params.dict()
        return Response(get_arithmetic_result(data, self.api_name))
    def post(self, request):
        return Response(get_arithmetic_result(request.data, self.api_name))



def get_arithmetic_result(input_data, mode):
    serializer = CalcSerializer(data=input_data)
    if serializer.is_valid():
        result = calculator(serializer.data['op'], serializer.data['a'], serializer.data.get('b', 0))
    else:
        raise APIException(serializer.errors)
    return result
