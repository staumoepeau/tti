# -*- coding: utf-8 -*-
# Copyright (c) 2021, Sione Taumoepeau and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import math
import frappe
from frappe import _
from frappe.utils import cstr, formatdate, cint, getdate, date_diff, add_days, time_diff_in_hours, rounded, now


def get_app_name():
    frappe.db.set_value('System Settings', 'System Settings', 'app_logo','/files/TTI_Logo.png')
    frappe.db.set_value('System Settings', 'System Settings', 'app_name', 'TTI MIS')

