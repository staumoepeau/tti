# -*- coding: utf-8 -*-
# Copyright (c) 2021, Sione Taumoepeau and contributors
# For license information, please see license.txt

#from __future__ import unicode_literals
#import math
#import frappe
#from frappe import _
#from frappe.utils import cstr


#@frappe.whitelist(allow_guest=True)
#def get_permission_query_conditions_for_student(user):
#    if not user: user = frappe.session.user
    
#    if user == "Administrator":
#        return ""
#    else:
#        return """(`tabStudent`.user = '{user}')""" .format(user=user)


#def has_permission(user):
#    if not user: user = frappe.session.user
#    if (user != "Administrator"):
        # dont allow non Administrator user to view / edit Administrator user
#        return True

#def get_permission_query_conditions_for_program_enrollment(user):

#    if not user: user = frappe.session.user 
    
#    if user == "Administrator":
#        return ""
#    else:
#        user = frappe.db.get_value("Student",{"user": frappe.session.user},"name")
#        return """(`tabProgram Enrollment`.student = '{user}')""" .format(user=user)