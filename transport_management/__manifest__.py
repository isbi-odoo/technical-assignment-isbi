# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name':'Transport Management',
    'depends':[
        'fleet','stock_picking_batch','stock',
    ],
    'installable':True,
    'application':True,

    'data':[
        'security/ir.model.access.csv',
        'views/transport_menu.xml',
        'views/transport_fleet_category_view.xml',
        'views/transport_batch_transfer_view.xml',
        'views/transport_stock_picking_view.xml',
        # 'views/transport_menu.xml',
    ],
}