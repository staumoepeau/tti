// Copyright (c) 2023, Sione Taumoepeau and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["TTI Transcript"] = {
	"filters": [
		{   
			"fieldname": "student",
			"label": __("Student"),
			"fieldtype": "Link",
			"options": "Student",
			"width": "100px",
			"reqd": 1,
			on_change: () => {
				var student = frappe.query_report.get_filter_value('student');
				
				if (student) {
					frappe.db.get_value('Student', student, ["title"], function(value) {
					frappe.query_report.set_filter_value('title', value["title"].toUpperCase());
					});
				}
			},
		},
		{
			"fieldname": "title",
			"label": __("Student Name"),
			"fieldtype": "Data",
			"read_only": 0
		},

	]
};
