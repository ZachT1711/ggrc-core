# Copyright (C) 2015 Google Inc., authors, and contributors <see AUTHORS file>
# Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
# Created By: anze@reciprocitylabs.com
# Maintained By: anze@reciprocitylabs.com

scope = "System"
description = """
  This role grants a user basic object creation and editing permission.
  """
permissions = {
    "read": [
        "Audit",
        "Categorization",
        "Category",
        "ControlCategory",
        "ControlAssertion",
        "Control",
        "ControlAssessment",
        "Issue",
        "DataAsset",
        "Directive",
        "Contract",
        "Policy",
        "Regulation",
        "Standard",
        "Document",
        "Facility",
        "Help",
        "Market",
        "Objective",
        "ObjectDocument",
        "ObjectOwner",
        "ObjectPerson",
        "Option",
        "OrgGroup",
        "Vendor",
        "PopulationSample",
        "Product",
        "Project",
        "Relationship",
        "RelationshipType",
        "SectionBase",
        "Section",
        "Clause",
        "SystemOrProcess",
        "System",
        "Process",
        "Person",
        "Program",
        "Role",
        "Context",
        {
            "type": "BackgroundTask",
            "terms": {
                "property_name": "modified_by",
                "value": "$current_user"
            },
            "condition": "is"
        },
    ],
    "create": [
        "Audit",
        "Workflow"
        "Categorization",
        "Category",
        "ControlCategory",
        "ControlAssertion",
        "Control",
        "ControlAssessment",
        "Issue",
        "DataAsset",
        "Directive",
        "Contract",
        "Policy",
        "Regulation",
        "Standard",
        "Document",
        "Facility",
        "Help",
        "Market",
        "Objective",
        "ObjectDocument",
        "ObjectPerson",
        "Option",
        "OrgGroup",
        "Vendor",
        "PopulationSample",
        "Product",
        "Project",
        "Relationship",
        "RelationshipType",
        "SectionBase",
        "Section",
        "Clause",
        "SystemOrProcess",
        "System",
        "Process",
        "ObjectOwner",
        "Person",
        "Program",
        "Role",
        "UserRole",
        "Request",
        "Response",
        "Context",
        {
            "type": "BackgroundTask",
            "terms": {
                "property_name": "modified_by",
                "value": "$current_user"
            },
            "condition": "is"
        },
    ],
    "view_object_page": [
        "__GGRC_ALL__"
    ],
    "update": [
        "Audit",
        "Workflow"
        "Categorization",
        "Category",
        "ControlCategory",
        "ControlAssertion",
        "Control",
        "ControlAssessment",
        "Issue",
        "DataAsset",
        "Directive",
        "Contract",
        "Policy",
        "Regulation",
        "Standard",
        "Document",
        "Facility",
        "Help",
        "Market",
        "Objective",
        "ObjectDocument",
        "ObjectPerson",
        "Option",
        "OrgGroup",
        "Vendor",
        "PopulationSample",
        "Product",
        "Project",
        "Relationship",
        "RelationshipType",
        "SectionBase",
        "Section",
        "Clause",
        "SystemOrProcess",
        "System",
        "Process",
        "ObjectOwner",
        "Program",
        "Role",
        "UserRole",
        "Request",
        "Response",
        "Context",
        {
            "type": "BackgroundTask",
            "terms": {
                "property_name": "modified_by",
                "value": "$current_user"
            },
            "condition": "is"
        },
    ],
    "delete": [
        "Audit",
        "Workflow"
        "Categorization",
        "Category",
        "ControlCategory",
        "ControlAssertion",
        "Control",
        "ControlAssessment",
        "Issue",
        "DataAsset",
        "Directive",
        "Contract",
        "Policy",
        "Regulation",
        "Standard",
        "Document",
        "Facility",
        "Help",
        "Market",
        "Objective",
        "ObjectDocument",
        "ObjectPerson",
        "Option",
        "OrgGroup",
        "Vendor",
        "PopulationSample",
        "Product",
        "Project",
        "Relationship",
        "RelationshipType",
        "SectionBase",
        "Section",
        "Clause",
        "SystemOrProcess",
        "System",
        "Process",
        "ObjectOwner",
        "Program",
        "Role",
        "UserRole",
        "Request",
        "Response",
        "Context",
        {
            "type": "BackgroundTask",
            "terms": {
                "property_name": "modified_by",
                "value": "$current_user"
            },
            "condition": "is"
        },
    ]
}
