# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Romain Deheele
#    Copyright 2015 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Street3 in lead addresses',
    'version': '8.0.0.1.0',
    'author': "Camptocamp,Odoo Community Association (OCA)",
    'maintainer': 'Camptocamp',
    'category': 'Customer Relationship Management',
    'complexity': 'easy',
    'depends': ['partner_address_street3', 'crm'],
    'website': 'http://www.camptocamp.com',
    'data': ['view/crm_lead_view.xml'],
    'demo': [],
    'test': ['test/test_street3.yml'],
    'installable': False,
    'auto_install': False,
    'license': 'AGPL-3',
    'application': False,
}
