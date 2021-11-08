from django.shortcuts import render
from rest_framework.views  import  APIView
from rest_framework.response import Response
from rest_framework import status
from resume.models import  Personal_Data, Language
from resume.serializers import  Personal_DataSerializer, LanguageSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework import exceptions
from django.conf import settings


class Personal_DataAPIView(APIView):
    
    def post(self, request):
        serializer = Personal_DataSerializer(data=request.data )
        if serializer.is_valid():
            
            personal_Data = Personal_Data.objects.create(
                image = serializer.validated_data.get('image'),
                position_applied_for = serializer.validated_data.get('position_applied_for'),
                num_passport_expire = serializer.validated_data.get('num_passport_expire'),
                full_name = serializer.validated_data.get('full_name'),
                nationality_gender = serializer.validated_data.get('nationality_gender'),
                country_city_of_residence = serializer.validated_data.get('country_city_of_residence'),
                date_and_place_of_birth = serializer.validated_data.get('date_and_place_of_birth'),
                age_height_weight = serializer.validated_data.get('age_height_weight'),
                status_children = serializer.validated_data.get('status_children'),
                health_smoker = serializer.validated_data.get('health_smoker'),
                image_full_height = serializer.validated_data.get('image_full_height'))
            
            serializer = Personal_DataSerializer(instance=personal_Data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LanguageAPIView(APIView):

    def post(self, request):
        serializer = LanguageSerializer(data=request.data )
        if serializer.is_valid():
            
            language = Language.objects.create(
                
                language = serializer.validated_data.get('language'),
                written = serializer.validated_data.get('written'),
                spoken  = serializer.validated_data.get('spoken'),
                understanding  = serializer.validated_data.get('understanding'))
            
            serializer = Personal_DataSerializer(instance=language)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)





# from docx import Document
# from django.http import HttpResponse
# from docx  import Inches
# from docx.shared import Inches
# import date

# def TestDocument(request):

#     document = Document()
    
#     docx_title="TEST_DOCUMENT.docx"
    
#     # ---- Cover Letter ----
#     document.add_picture((r'%s/static/images/my-header.png' % (settings.PROJECT_PATH)), width=Inches(4))
#     document.add_paragraph()
#     document.add_paragraph("%s" % date.today().strftime('%B %d, %Y'))

#     document.add_paragraph('Dear Sir or Madam:')
#     document.add_paragraph('We are pleased to help you with your widgets.')
#     document.add_paragraph('Please feel free to contact me for any additional information.')
#     document.add_paragraph('I look forward to assisting you in this project.')

#     document.add_paragraph()
#     document.add_paragraph('Best regards,')
#     document.add_paragraph('Acme Specialist 1]')
#     document.add_page_break()

#     # Prepare document for download        
#     # -----------------------------
#     f = StringIO()
#     document.save(f)
#     length = f.tell()
#     f.seek(0)
#     response = HttpResponse(
#         f.getvalue(),
#         content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
#     )
#     response['Content-Disposition'] = 'attachment; filename=' + docx_title
#     response['Content-Length'] = length
#     return response


    
    
    
    
    
    
    
    # @swagger_auto_schema(operations_description='Upload thumbnail',
    # request_body=LanguageSerializer, methods=['post'])
    # @api_view(['POST'])
    # def post(self, request):
    #     serializer =  LanguageSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     language = serializer.validated_data.get('language')
    #     written = serializer.validated_data.get('written')
    #     spoken  = serializer.validated_data.get('spoken')
    #     understanding  = serializer.validated_data.get('understanding')
       
    
    #     languags = Language.objects.create(language=language, written=written, spoken=spoken,
    #                                     understanding=understanding)
    #     return Response({'message': 'true'})

