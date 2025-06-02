case_fields= [
    "Id",
    "CaseNumber", 
    "AE_FX_Status__c",
    "AE_CM_FX_CreatedDate__c",
    "Subject", 
    "AE_Type__c",
    "Type",
    "Origin",
    "SuppliedName"]

case_fields_def= [
    "Request Number", 
    "Status",
    "Opened",
    "Subject", 
    "Type",
    "Request Type",
    "Source",
    "Requestor"]



order_fields_def = [#"AE_CM_Order__r.Sales_Order_Number__c",
    "Order Number",
    "Booked",
    "End User",
    "Vendor",
    "Partner PO Number",
    "Status",
    "Total Price",
    "Type",
    "Source",
    "Ordered Date",
    "Created Date",
    "Region"]

order_fields=[
    "AE_CM_Order__r.Id",
    "AE_CM_Order__r.Name",
    "AE_CM_Order__r.AE_Booked_Date__c",
    "AE_CM_Order__r.End_User_Name__c",
    "AE_CM_Order__r.AE_TXT_VendorName__c",
    "AE_CM_Order__r.AE_Partner_PO__c",
    "AE_CM_Order__r.AE_FX_Status__c",
    "AE_CM_Order__r.AE_Order_Total__c",
    "AE_CM_Order__r.AE_Arrow_SO_Type__c",
    "AE_CM_Order__r.AE_Order_Source_Type__c",
    "AE_CM_Order__r.AE_Ordered_Date__c",
    "AE_CM_Order__r.AE_Creation_Date__c",
    "AE_CM_Order__r.AE_FX_Region__c"
    
]

quote_fields = [#"ECS_Quote__r.Quote_Number__c",
    "ECS_Quote__r.Id",
    "ECS_Quote__r.Quote_Number__c",
    "ECS_Quote__r.AE_TXT_Quote_Full_Name__c",
    "ECS_Quote__r.Quote_Name__c",
    "ECS_Quote__r.AE_VendorName__c",
    "ECS_Quote__r.End_Customer__c",
    "ECS_Quote__r.AE_TXT_Status__c",
    "ECS_Quote__r.AE_TXT_Region__c",
    "ECS_Quote__r.AE_TXT_Renewal_Value__c",
    "ECS_Quote__r.AE_Total_Price__c",
    "ECS_Quote__r.Quote_Expire_Date__c",
    "ECS_Quote__r.Creation_Date__c",
    "ECS_Quote__r.Primary__c",
    "ECS_Quote__r.SalesRep_Name__c",
    "ECS_Quote__r.AE_Reseller_PO__c"
]

quote_fields_def = [#"ECS_Quote__r.Quote_Number__c",
    
    "Quote No.",
    "Quote Full Name",
    "Name",
    "Vendor",
    "End User",
    "Status",
    "Region",
    "Type",
    "Total Price",
    "Expiry date",
    "Creation date",
    "Primary", 
    "Sales rep",
    "Channel Partner PO#"
]

invoice_fields=[
"AE_CM_Invoice__r.Id",
"AE_CM_Invoice__r.Name",
"AE_CM_Invoice__r.AE_InvoiceTypeCode_value__c",
"AE_CM_Invoice__r.AE_VendorName__c",
"AE_CM_Invoice__r.AE_Invoice_Date__c",
"AE_CM_Invoice__r.AE_Arrow_SO__c",


"AE_CM_Invoice__r.AE_Partner_Purchase_Order__c",
"AE_CM_Invoice__r.AE_End_User_Name__c",

"AE_CM_Invoice__r.AE_PP_FX_AccountOracleNumber__c",
"AE_CM_Invoice__r.AE_Invoice_Currency_Code__c",
"AE_CM_Invoice__r.AE_Total_Amount__c",
"AE_CM_Invoice__r.AE_Invoice_Source_Type__c",
"AE_CM_Invoice__r.AE_FX_Invoice_Status__c",
"AE_CM_Invoice__r.AE_PP_RemainingAmount__c",


]

invoice_fields_def = [
    
    "Invoice#",
    "Type",
    "Vendor",
    "Received on",
    "Arrow SO#",
    "Partner PO#",
    "End User",
    "Account No.",
    "Currency",
    "Invoice Amount",
    "Source",
    "Status",
    "Balance"
]

columns =case_fields+quote_fields+order_fields+invoice_fields
condition_column = ["CaseNumber","ECS_Quote__r.Quote_Number__c",
                        "AE_CM_Order__r.Name",
                        "AE_CM_Invoice__r.Name",
                        "AE_CM_Order__r.AE_Partner_PO__c"]
SAFE_FIELDS = ["CaseNumber","ECS_Quote__r.Quote_Number__c",
                        "AE_CM_Order__r.Name",
                        "AE_CM_Invoice__r.Name",
                        "AE_CM_Order__r.AE_Partner_PO__c"]
SAFE_OBJECT = "Case"
table_name = "Case"
case_fields_ = case_fields[1:]

order_fields_ = [i.split(".")[1] for i in order_fields[1:]]
po_order_fields_ = [i.split(".")[1] for i in order_fields[1:]]

quote_fields_ = [i.split(".")[1] for i in quote_fields[1:]]

invoice_fields_ = [i.split(".")[1] for i in invoice_fields[1:]]


case_def_dict = dict(zip(case_fields_,case_fields_def))

order_def_dict = dict(zip(order_fields_,order_fields_def))
invoice_def_dict = dict(zip(invoice_fields_,invoice_fields_def))

quote_def_dict = dict(zip(quote_fields_,quote_fields_def))
po_order_def_dict = dict(zip(order_fields_,order_fields_def))







