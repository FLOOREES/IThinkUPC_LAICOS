from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.contrib.auth.decorators import login_required
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,  logout
from django.http import HttpResponseRedirect
from .forms import NameForm
import string
import random
import names

import subprocess
from django.http import JsonResponse
from pathlib import Path
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.shortcuts import render

from kmodes.kprototypes import KPrototypes
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

@login_required
def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
@login_required
def details(request, slug):
  mymember = Member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


@login_required
def main(request):
  template = loader.get_template('main.html')
  print(request.user.is_authenticated)
  context = {
    'user': request.user,
  }
  return HttpResponse(template.render(context,request))


def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
			messages.success(request, "Registration successful." )
			return HttpResponseRedirect('/')
		messages.error(request, "Unsuccessful registration. Invalid information.")
		   
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				print(f"You are now logged in as {username}.")
				messages.info(request, f"You are now logged in as {username}.")
				return HttpResponseRedirect('/questions/')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_form":form})
@login_required
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/")
@login_required
def questions_request(request):
	
	
	print(Member.objects.all().values())
	template = loader.get_template('questions.html')
	context = {
    'user': request.user,
  	}

	r = True
	for e in Member.objects.all().values():
		if (str(e['username']) == str(context["user"])):
			r = False
	if r:
		l = request.POST.get("name")
		print(context["user"])
		if (l is not None) and r:
			new_member = Member(username = request.user, 
				firstname = l, 
				age=request.POST.get("age"),
				degree = request.POST.get("degree"),
					music = request.POST.get("music"),
					sport = request.POST.get("sport"),
					read = request.POST.get("read"),
					board_games= request.POST.get("board"),)
			new_member.slug = str(new_member.firstname) + "-" + str(new_member.music)
			new_member.save()
			l = None
		return HttpResponse(template.render(context, request))
	else:
		return redirect("/")


def clear_request(request):
	Member.objects.all().delete()
	return redirect("/")

@login_required
def chat_request(request):
	template = loader.get_template('chat.html')
	context = {
    	'user': request.user,
  	}
	return HttpResponse(template.render(context, request))


def generate_request(request):
	def get_random_string(length):
		# choose from all lowercase letter
		letters = string.ascii_lowercase
		result_str = ''.join(random.choice(letters) for i in range(length))
		return result_str

	degrees = ['GIA', 'GEI', 'GCED']
	musics = ['pop', 'reggateon', 'jazz', 'classical', 'other', 'rock', 'techno']
	for _ in range(49):
		new_member = Member(username = get_random_string(9), 
					firstname = names.get_first_name() + "_" + names.get_last_name(), 
					age=random.randint(18,34),
					degree = degrees[random.randint(0,2)],
						music = musics[random.randint(0, 6)],
						sport = random.randint(1,10),
						read = random.randint(1,10),
						board_games= random.randint(1,10),)
		new_member.slug = str(new_member.firstname) + "-" + str(new_member.music)
		new_member.save()

	return redirect("/")

@csrf_exempt
def myscript(request):
    read_db()
    #print(result)
    #output = result.stdout.strip()  # Eliminar espacios en blanco alrededor del texto
    return redirect("/")

from django.shortcuts import render, redirect

def register_study_slot(request):
    if request.method == "POST":
        study_slot = request.POST.get("study_slot")
        # Realizar las operaciones necesarias con la franja horaria seleccionada
        # Por ejemplo, puedes crear un nuevo objeto de franja horaria y asociarlo al usuario actual
        # Aquí puedes realizar consultas a la base de datos y ejecutar las acciones necesarias
        
        # Ejemplo: Crear un nuevo objeto de franja horaria asociado al usuario
        user = request.user
        # Código para crear el objeto de franja horaria y guardarlo en la base de datos
        
        # Redireccionar a una página de confirmación o a otra sección de la aplicación
        return redirect("confirmation_page")
    

from kmodes.kprototypes import KPrototypes

from kmodes.kprototypes import KPrototypes
from sklearn.preprocessing import OneHotEncoder

from kmodes.kprototypes import KPrototypes
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def read_db():
    # Obtén el queryset de los miembros
    print("holagupao")
    members_queryset = Member.objects.all()[:50]
    print("aqui")
    # Verifica si hay miembros en el queryset
    if not members_queryset:
        print("No hay miembros en el queryset.")
        return

    # Crea una lista para almacenar los datos de los miembros
    data = []

    # Recorre el queryset y obtén los datos de los miembros
    for member in members_queryset:
        member_data = member.__dict__.copy()  # Obtiene todos los atributos del objeto Member
        member_data.pop('_state', None)  # Elimina el atributo _state
        data.append(member_data)

    # Crea un DataFrame con los datos
    df = pd.DataFrame(data)

    # Selecciona los atributos relevantes para el clustering
    categorical_features = df.select_dtypes(include='object').columns.tolist()

    # Preprocesamiento de datos
    # Codificación one-hot de los atributos categóricos
    encoder = OneHotEncoder()
    encoded_categorical = encoder.fit_transform(df[categorical_features])
    encoded_df = pd.DataFrame(encoded_categorical.toarray(), columns=encoder.get_feature_names_out(categorical_features))

    # Combina los atributos categóricos codificados con los atributos numéricos originales
    preprocessed_df = pd.concat([df.drop(categorical_features, axis=1), encoded_df], axis=1)

    # Crea una matriz de características con los atributos relevantes
    attributes = preprocessed_df.columns.tolist()
    X = preprocessed_df.values

    # Especifica el número de clusters (K)
    n_clusters = 10

    # Crea y ajusta el modelo K-prototypes
    kproto = KPrototypes(n_clusters=n_clusters)
    clusters = kproto.fit_predict(X, categorical=list(range(len(categorical_features))))

    # Agrupación de miembros por intereses y semejanzas
    member_clusters = {}
    for idx, member in enumerate(members_queryset):
        cluster_label = clusters[idx]  # Etiqueta de clúster asignada al miembro
        if cluster_label not in member_clusters:
            member_clusters[cluster_label] = []  # Inicializa una lista vacía para el clúster si no existe
        member_clusters[cluster_label].append(member)  # Agrega el miembro a la lista del clúster correspondiente

    # Imprime las etiquetas de clúster asignadas a cada miembro
    # Imprime los grupos de miembros por intereses y semejanzas
    for cluster_label, members in member_clusters.items():
	
        print(f"Cluster {cluster_label}:")
        for member in members:
            member.cluster = cluster_label
            member.save()
