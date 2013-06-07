from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from urllib import quote_plus as urlquote, unquote
from sqlalchemy.engine import create_engine
from sqlalchemy import orm
from sqlalchemy import *
from sqlalchemy.sql import *
from dbmap.models import TablesData, Databases, FieldData, RecordData
from dbmap.forms import DatabaseForm
import os
import sys
from upload import upload_handle
from save_table import save_field, save_record


def index(request):
    databases = Databases.objects.all()
    context = {'databases': databases}
    return render_to_response('index.html', context, context_instance=RequestContext(request))


def add_db(request):
    form = DatabaseForm()
    context = {'form': form}
    if request.method == 'POST':
        form = DatabaseForm(request.POST)
        db = request.POST['name']
        host = request.POST['host']
        name = request.POST['user']
        passwd = request.POST['passwd']
        db_type = request.POST['type']
        if 'SQ' in request.POST['type']:
            path = request.FILES['path']
            path = upload_handle(path)
            strd = 'sqlite:///%s' % path
        else:
            strd = 'mysql://%s:%s@%s/%s' % (urlquote(name), urlquote(passwd), urlquote(host), urlquote(db))
        ##return render_to_response('database.html', context, context_instance=RequestContext(request))
        messages = []
        metadata = MetaData()
        #strd = 'mysql://%s:%s@%s/%s' % (urlquote(name), urlquote(passwd), urlquote(host), urlquote(db))
        engine = create_engine(strd)
        Session = orm.sessionmaker(bind=engine)
        session = Session()
        connection = engine.connect()
        tab = []
        instance = Databases(name=db, db_type=db_type, user=name, passwd=passwd, host=host)
        instance.save()
        print engine.table_names()
        for t in engine.table_names():
            print t
            tab.append(t)
            messages = Table(t, metadata, autoload=True, autoload_with=engine)
            s = messages.select()
            result = connection.execute(s)
            #print result
            tb = TablesData(db=instance, name=t, row_count=session.query(messages).count(), column_count=len(messages.columns.items()), decription='')
            tb.save()
            save_field(messages, tb)
            save_record(messages, tb, session)
        return HttpResponseRedirect('/')
    return render_to_response('database.html', context, context_instance=RequestContext(request))


def view_fields(request):
    value = 0
    if request.method == 'POST':
        id_data = request.POST['database']
        value = id_data
        databases = Databases.objects.get(pk=id_data)
        print databases.name
        tables = databases.tablesdata_set.all()
        fields = FieldData.objects.all()
        databases = Databases.objects.all()
    else:
        fields = FieldData.objects.all()
        tables = TablesData.objects.all()
        databases = Databases.objects.all()
    context = {'fields': fields, 'tables': tables, 'i': 0, 'databases': databases, 'value': value}
    return render_to_response('fields.html', context, context_instance=RequestContext(request))


def view_records(request):
    value = 0
    if request.method == 'POST':
        id_data = request.POST['database']
        value = id_data
        databases = Databases.objects.get(pk=id_data)
        print databases.name
        tables = databases.tablesdata_set.all()
        records = RecordData.objects.all()
        databases = Databases.objects.all()
    else:
        records = RecordData.objects.all()
        tables = TablesData.objects.all()
        databases = Databases.objects.all()
    context = {'records': records, 'tables': tables, 'i': 0, 'databases': databases, 'value': value}
    return render_to_response('records.html', context, context_instance=RequestContext(request))


def view_tables(request):
    tables = TablesData.objects.all()
    context = {'tables': tables}
    return render_to_response('tables.html', context, context_instance=RequestContext(request))
