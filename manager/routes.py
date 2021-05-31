from socket import gethostname

from flask import request, render_template, redirect, url_for, flash

from manager import app
from manager.models import RouteTable, NetworkInterfaces
from manager.forms import RouteTableForm, NetworkInterfacesForm
from manager.structures import Route, Address


@app.get('/')
def index():
    return render_template('index.html',
                           title='Main',
                           hostname=gethostname(),
                           routes=RouteTable.static_routes(),
                           addresses=NetworkInterfaces.addresses())


@app.get('/routes')
@app.post('/routes')
def routes():
    form = RouteTableForm()
    if form.validate_on_submit():
        dst, prefix = form.dst.data.split('/')
        route = Route(dst=dst,
                      prefix=int(prefix),
                      gateway=form.gateway.data)
        RouteTable.add_route(route)
        flash(f'Route "{route}" has been added', 'success')
        return redirect(url_for('routes'))
    return render_template('routes.html',
                           title='Routes',
                           hostname=gethostname(),
                           form=form,
                           routes=RouteTable.static_routes(),
                           networks=RouteTable.onlink_routes())


@app.get('/routes/delete')
def route_delete():
    route = Route(dst=request.args.get('dst'),
                  prefix=int(request.args.get('prefix')),
                  gateway=request.args.get('gateway'),
                  ifindex=int(request.args.get('ifindex')),
                  ifname=request.args.get('ifname'))
    flash(f'Route "{route}" has been deleted', 'success')
    RouteTable.delete_route(route)
    return redirect(url_for('routes'))


@app.get('/addresses')
@app.post('/addresses')
def addresses():
    form = NetworkInterfacesForm()
    if form.validate_on_submit():
        ip, prefix = form.address.data.split('/')
        address = Address(ip=ip,
                          prefix=int(prefix),
                          ifname=form.ifname.data)
        NetworkInterfaces.add_address(address)
        flash(f'Address "{address}" has been added', 'success')
        return redirect(url_for('addresses'))
    return render_template('addresses.html',
                           title='Addresses',
                           hostname=gethostname(),
                           form=form,
                           addresses=NetworkInterfaces.addresses())


@app.get('/addresses/delete')
def address_delete():
    address = Address(ip=request.args.get('ip'),
                      prefix=int(request.args.get('prefix')),
                      ifindex=int(request.args.get('ifindex')),
                      ifname=request.args.get('ifname'))
    NetworkInterfaces.delete_address(address)
    flash(f'Address "{address}" has been deleted', 'success')
    return redirect(url_for('addresses'))
