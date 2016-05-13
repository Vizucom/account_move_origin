# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2016- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Invoice Origin Field for Journal Entries',
    'category': 'Accounting & Finance',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'depends': ['account'],
    'description': """
Invoice Origin Field for Journal Entries
========================================
* Shows the related invoice's origin field on journal Entries (e.g. which sale order the invoice originated from)

""",
    'data': [
        'views/account_move.xml',
    ],
}
