# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name':'Transport',
    'depends':[
        'fleet','stock_picking_batch','stock',
    ],
    'installable':True,
    'application':True,

    'data':[
        'views/transport_fleet_category_view.xml',
        'views/transport_batch_transfer_view.xml',
        'views/transport_stock_picking_view.xml',
    ],
}