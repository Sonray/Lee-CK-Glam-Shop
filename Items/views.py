from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Reviews, Product_details
from .serializers import ProductSerializer, ReviewSerializer
from rest_framework.decorators import permission_classes
from rest_framework import permissions, generics, status, filters
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

# Create your views here.


@permission_classes((permissions.IsAuthenticated, TokenHasReadWriteScope))
class Display_all_products(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    
    def get(self, request, format=None):
        all_post = Product_details.objects.all()
        serializers = ProductSerializer(all_post, many=True)
        return Response(serializers.data)
        
        
@permission_classes((permissions.IsAuthenticated, TokenHasScope, TokenHasReadWriteScope ))
class Display_specific_product(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    
    def get_object(self,pk):
        '''
        retrieve product object from database
        '''

        try:
            return Product_details.objects.get(pk=pk)
        except Product_details.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        '''
        get a single product object with its details
        '''

        product=self.get_object(pk)
        serializers=ProductSerializer(product)
        return Response(serializers.data) 


@permission_classes((permissions.IsAuthenticated, TokenHasScope, TokenHasReadWriteScope))
class Make_a_review(APIView):    

    serializer_class = ReviewSerializer

    def post(self, request, format=None):
        
        review = request.data
        serializers = self.serializer_class(data=review)

        if serializers.is_valid(raise_exception=True):

            serializers.create(request)

            return Response(
                serializers.data, status=status.HTTP_201_CREATED
                )
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.IsAuthenticated, TokenHasScope, TokenHasReadWriteScope )) 
class Display_all_Reviews(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    def get_object(self,pk):
        '''
        retrieve product object from database
        '''

        try:
            return Reviews.objects.filter(product=pk)
        except Reviews.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, format=None):
        '''
        get a single product object with its details
        '''

        review=self.get_object(pk)
        serializers=ReviewSerializer(review, many=True)
        return Response(serializers.data) 


@permission_classes((permissions.IsAuthenticated, TokenHasScope, TokenHasReadWriteScope )) 
class Search_products_category(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    
    queryset = Product_details.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['category__category']
    
    
@permission_classes((permissions.IsAuthenticated, TokenHasScope, TokenHasReadWriteScope)) 
class Search_products_subcategory(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    
    queryset = Product_details.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['sub_category__sub_category']
    
    
@permission_classes((permissions.IsAuthenticated, TokenHasScope, TokenHasReadWriteScope)) 
class Search_products(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    
    queryset = Product_details.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [ '^sub_category__sub_category', '^sub_category__sub_category',
                     '^product_description', '^product_name', 'new_price',
                     '^specifications__product_specification', '^key_features__product_feature' ]
    

