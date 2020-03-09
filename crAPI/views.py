from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import RequestForm
from . serializers import RequestFormSerializers
import pickle
from sklearn.externals import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
from sklearn.neighbors import NearestNeighbors

from keras.models import Model
from keras.layers import Dense, Input
from keras.datasets import mnist
from keras.regularizers import l1
from keras.optimizers import Adam

import tensorflow as tf

from . forms import SubmissionForm

from django.contrib import messages




class RequestFormView(viewsets.ModelViewSet):
	queryset = RequestForm.objects.all()
	serializer_class = RequestFormSerializers
		
def approvereject(unit):
	try:
		raw_df = pd.read_csv('crAPI/raw_df.csv')
		raw_df = raw_df.iloc[:,2:].drop(['OS', 'year'],axis=1)
		mdl = joblib.load('crAPI/company_recommender.pkl')
		data = pd.read_csv('crAPI/encoded_data.csv')
		data2=data
		data.reset_index()
		data = data.drop(['Unnamed: 0'], axis = 1)
		x_train = data

		hidden_size = 46
		input_dimension=69
		code_size=23
		epochs=10
		#Establishing neural network layers
		input_img = Input(shape=(input_dimension,))
		hidden_1 = Dense(hidden_size, activation='relu')(input_img)
		hidden_2 = Dense(23, activation='relu')(hidden_1)
		code = Dense(code_size, activation='relu')(hidden_2) #---------------> Hidden layer 
		hidden_3 = Dense(23, activation='relu')(code)
		hidden_4 = Dense(hidden_size, activation='relu')(hidden_3)
		output_img = Dense(input_dimension, activation='sigmoid')(hidden_4)

		#Declaring Encoder 
		encoder = Model(input_img, code)
		autoencoder=Model(input_img, output_img)
		autoencoder.compile(loss='binary_crossentropy',optimizer='adam')
		autoencoder.fit(x_train, x_train, epochs=epochs)
		mdl = encoder.predict(data)
		mydata=unit
		column_data=list(mydata.values())
		print(column_data)

		company_name=column_data[6]
		column_data=column_data[1:]
		print(column_data)
		new_data_point = pd.DataFrame([column_data], columns=raw_df.columns)
		new_data_point.fillna({'Featured Report?':'No', \
           'GOLD Community': 'No', \
           'Listed/Non-listed': 'Listed', \
           'OS':'No', \
           'Organization type': 'Private Company', 
           'Size': 'Large'}, inplace=True)

		data_clean = new_data_point.drop(['Name'], axis=1).loc[:,'Country Status':'Size']
		features_dataframe = data_clean.copy()
		for feature in data_clean.columns:
		    dfDummies = pd.get_dummies(data_clean[feature], prefix = feature)
		    features_dataframe = pd.concat([features_dataframe, dfDummies], axis=1)

		ncolumns_data = len(data_clean.columns)
		code_columns = list(features_dataframe.columns)[ncolumns_data:]
		one_hot_encoded=features_dataframe[code_columns].copy()

		#shaping datapoint to 69 columns
		original_one_hot_encoded_df = data2
		original_one_hot_encoded_df = original_one_hot_encoded_df.iloc[:,1:]
		one_hot_encoded_shaped = pd.concat([original_one_hot_encoded_df, one_hot_encoded], ignore_index = True, sort = True)
		# this part weird alr ^

		one_hot_encoded_shaped = one_hot_encoded_shaped[-1:].fillna(int(0))
		#one_hot_encoded_shaped=one_hot_encoded_shaped.iloc[:,:-3]
		
		#compressing one hot encoded features
		compressed_features = encoder.predict(one_hot_encoded_shaped)
		#Clustering Algorithm -> K-Nearest-Neighbors (k=5)
		combined_encoded_points = np.append(mdl, compressed_features,axis=0)
		knn = NearestNeighbors(n_neighbors=6)
		knn.fit(combined_encoded_points)
		neighbors = knn.kneighbors(combined_encoded_points[len(combined_encoded_points)-1].reshape(1,-1))        

		index_df = pd.DataFrame(neighbors[1]).T
		index_df.columns = ['Index']

		print('\n')
		print("Your selected company is: "+str(company_name))
		print('Your reccomended companies are: ')    
		print("Index \t Company Name")
		finalstring=''
		
		if index_df['Index'][0] == 12491:
		    for i in range (1,6):
		        z = index_df['Index'][i]
		        finalstring = finalstring + '○' + str(raw_df.iloc[z]['Name'])



		        # finalstring = finalstring +  str(raw_df.iloc[z]['Name'] + '\t' + '\n')
		       	#print(str(index_df['Index'][i]) + '\t '+ raw_df.iloc[z]['Name'])
		    return finalstring

		else:
		    for i in range (0,5):
		        z = index_df['Index'][i]
		        finalstring = finalstring + '○' + str(raw_df.iloc[z]['Name'])
		       
		       #finalstring = finalstring +  str(raw_df.iloc[z]['Name'] + '\t' + '\n')

		        #print(str(index_df['Index'][i]) + '\t ' + raw_df.iloc[z]['Name'])
		        messages.success(unit,finalstring)
		    return finalstring

	except ValueError as e:
		errorstring='Please Try Again Later'
		return errorstring

def cxcontact(request):
	if request.method=='POST':
		form=SubmissionForm(request.POST)
		if form.is_valid():
			coyname=form.cleaned_data['coyname']
			countryname=form.cleaned_data['countryname']
			countrystatus=form.cleaned_data['countrystatus']
			featurereport=form.cleaned_data['featurereport']
			goldcommunity=form.cleaned_data['goldcommunity']
			companylisted=form.cleaned_data['companylisted']
			organisationtype=form.cleaned_data['organisationtype']
			sector=form.cleaned_data['sector']
			companysize=form.cleaned_data['companysize']
			myDict = (request.POST).dict()
			answer=approvereject(myDict)
			#messages.success(request,'{}'.format(answer))
			messages.info(request,coyname)
			messages.success(request,answer)
	form=SubmissionForm()

	return render(request, 'myform/cxform.html', {'form':form})

def home(request):
	return render(request,"index.html")



