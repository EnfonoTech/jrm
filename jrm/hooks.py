app_name = "jrm"
app_title = "Jrm"
app_publisher = "Enfono Technologies"
app_description = "Job Record Management"
app_email = "aravindr@enfono.in"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/jrm/css/jrm.css"
# app_include_js = "/assets/jrm/js/jrm.js"

# include js, css files in header of web template
# web_include_css = "/assets/jrm/css/jrm.css"
# web_include_js = "/assets/jrm/js/jrm.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "jrm/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Purchase Order": "public/js/purchase_order.js",
    "Sales Order": "public/js/sales_order.js",
    "Quotation": "public/js/quotation.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "jrm/public/icons.svg"

# Home Pages
# ----------
# app_include = [
#     "patches.override_payment_entry"
# ]
# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "jrm.utils.jinja_methods",
# 	"filters": "jrm.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "jrm.install.before_install"
# after_install = "jrm.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "jrm.uninstall.before_uninstall"
# after_uninstall = "jrm.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "jrm.utils.before_app_install"
# after_app_install = "jrm.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "jrm.utils.before_app_uninstall"
# after_app_uninstall = "jrm.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "jrm.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }
# override_doctype_class = {
#     "Expense Claim": "jrm.hrms_overrides.expense_claim.CustomExpenseClaim"
# }

# In your custom app's hooks.py
# doc_events = {
#     "*": {
#         "on_load": "jrm.hrms_overrides.expense_claim.override_methods"
#     }
# }
doc_events = {
	"Expense Request": {
		"on_update": "jrm.api.setup"
	},
    "Purchase Order": {
        "on_submit": "jrm.po_hooks.update_job_record_percent",
        "on_cancel": "jrm.po_hooks.update_job_record_percent",
        "on_amend": "jrm.po_hooks.update_job_record_percent"
    },
    "Purchase Invoice": {
        "on_submit": "jrm.po_hooks.update_job_record_percent",
        "on_cancel": "jrm.po_hooks.update_job_record_percent",
        "on_amend": "jrm.po_hooks.update_job_record_percent"
    },
    "Purchase Receipt": {
        "on_submit": "jrm.po_hooks.update_job_record_percent",
        "on_cancel": "jrm.po_hooks.update_job_record_percent",
        "on_amend": "jrm.po_hooks.update_job_record_percent"
    },
    "Sales Order": {
        "on_submit": "jrm.po_hooks.update_job_record_percent",
        "on_cancel": "jrm.po_hooks.update_job_record_percent",
        "on_amend": "jrm.po_hooks.update_job_record_percent"
    },
    "Sales Invoice": {
        "on_submit": "jrm.po_hooks.update_job_record_percent",
        "on_cancel": "jrm.po_hooks.update_job_record_percent",
        "on_amend": "jrm.po_hooks.update_job_record_percent"
    },
    "Delivery Note": {
        "on_submit": "jrm.po_hooks.update_job_record_percent",
        "on_cancel": "jrm.po_hooks.update_job_record_percent",
        "on_amend": "jrm.po_hooks.update_job_record_percent"
    }
}
# override_doctype_class = {
#     "Payment Entry": "jrm.overrides.CustomPE"    
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"jrm.tasks.all"
# 	],
# 	"daily": [
# 		"jrm.tasks.daily"
# 	],
# 	"hourly": [
# 		"jrm.tasks.hourly"
# 	],
# 	"weekly": [
# 		"jrm.tasks.weekly"
# 	],
# 	"monthly": [
# 		"jrm.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "jrm.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "jrm.event.get_events"
# }
# override_whitelisted_methods = {
#     "erpnext.accounts.doctype.payment_entry.payment_entry": "jrm.overrides.erpnext.accounts.doctype.payment_entry.payment_entry"
# }

# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "jrm.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["jrm.utils.before_request"]
# after_request = ["jrm.utils.after_request"]

# Job Events
# ----------
# before_job = ["jrm.utils.before_job"]
# after_job = ["jrm.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"jrm.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Custom fields for Sales Invoice
fixtures = [
    "Workflow", 
    "Workflow State", 
    "Workflow Action Master",
    {
        "dt": "Custom Field",
        "filters": [
            ["module", "=", "jrm"]
        ]
    }
]

