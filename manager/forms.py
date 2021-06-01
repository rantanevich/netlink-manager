from ipaddress import IPv4Address, IPv4Network

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, IPAddress, ValidationError

from manager.models import RouteTable, NetworkInterfaces


class RouteTableForm(FlaskForm):
    dst = StringField('Destination', validators=[DataRequired()])
    gateway = StringField('Gateway', validators=[DataRequired(), IPAddress()])
    submit = SubmitField('Apply')

    def validate_dst(form, field):
        try:
            if '/' not in field.data and IPv4Network(field.data):
                raise ValidationError('Subnet prefix isn\'t specified')

            if RouteTable.route_exists(field.data):
                raise ValidationError('Destination already exists')
        except ValueError as err:
            raise ValidationError(err)

    def validate_gateway(form, field):
        gateway = IPv4Address(field.data)

        if not any(gateway in IPv4Network(f'{network.dst}/{network.prefix}')
                   for network in RouteTable.onlink_routes()):
            raise ValidationError('Network is unreachable')


class NetworkInterfacesForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired()])
    ifname = SelectField('Interface', validators=[DataRequired()])
    submit = SubmitField('Apply')

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.ifname.choices = NetworkInterfaces.interfaces()

    def validate_address(form, field):
        try:
            if '/' not in field.data and IPv4Network(field.data):
                raise ValidationError('Subnet prefix isn\'t specified')

            if NetworkInterfaces.address_exists(field.data):
                raise ValidationError('Address already exists')
        except ValueError as err:
            raise ValidationError(err)
