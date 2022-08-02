# Copyright (c) 2021, Sione Taumoepeau and contributors
# For license information, please see license.txt
import json

import frappe
from frappe import _
from frappe.email.doctype.email_group.email_group import add_subscribers
from frappe.model.mapper import get_mapped_doc
from frappe.utils import cstr, flt, getdate

@frappe.whitelist()
def get_assessment_details(assessment_plan):
	"""Returns Assessment Criteria  and Maximum Score from Assessment Plan Master.

	:param Assessment Plan: Assessment Plan
	"""
	return frappe.get_all(
		"Assessment Plan Criteria",
		fields=["assessment_criteria", "maximum_score", "raw_marks", "docstatus"],
		filters={"parent": assessment_plan},
		order_by="idx",
	)

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