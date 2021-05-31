import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()
basedir = Path(__file__).parent


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')

    ROUTE_CONF = '/etc/sysconfig/network-scripts/route-'
    INTERFACE_CONF = '/etc/sysconfig/network-scripts/ifcfg-'
