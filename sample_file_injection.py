import requests
import logging
from .columns import columns,case_fields,order_fields,quote_fields,invoice_fields,\
case_def_dict,quote_def_dict,invoice_def_dict,order_def_dict,po_order_def_dict,\
    case_fields_,order_fields_,invoice_fields_,quote_fields_,po_order_fields_,condition_column,table_name,SAFE_FIELDS,SAFE_OBJECT
from collections import Counter

import urllib.parse
from .sql_query_validation import is_valid_sql

def case_status_details(case_id_list,case_history,instance_url,
                        access_token):
    
    
    c_list=""
    case_num=len(case_id_list)

    for i in range(0,case_num):
        if i==case_num-1:
            c_list=c_list+f"'{case_id_list[i]}','0{case_id_list[i]}'"
        else:
            c_list=c_list+f"'{case_id_list[i]}','0{case_id_list[i]}',"


    
    

    
    
    condition_values = case_id_list
    condition_values_str = ", ".join(f"'{val}'" for val in condition_values)
    
    if not all(col in SAFE_FIELDS for col in condition_column):
        print("Invalid Column Values")
        return " ",case_history,[]
    if table_name != SAFE_OBJECT:
        print("Invalid Object Value")
        return " ",case_history,[]

    
    
    where_conditions = [f"{col} IN ({condition_values_str})" for col in condition_column]

    where_clause = " OR ".join(where_conditions)
    
    # soql = {urllib.parse.quote(query)}
    response,_=get_res(columns,table_name,where_clause,instance_url, access_token)
    
    
    res2,case_history,id_list = extract_query_response(response,case_id_list,case_history)
    
    return res2,case_history,id_list
    
def extract_query_response(sf_query_response,qco_id_list,case_history):
    print("\n\n\n")
    print("---------------------------")
    case={}
    
    
    if(len(sf_query_response)>0):
        print("Case length  is not Zero")


        temp_str,case_history_updated,id_list = query_data_formatting(sf_query_response,qco_id_list,quote_def_dict,order_def_dict,
                            case_def_dict,invoice_def_dict,
                            po_order_def_dict,
                            quote_fields_,
                            order_fields_,
                            invoice_fields_,
                            po_order_fields_,
                            case_fields_,case_history)
        
        print(f"Temp_STR is {temp_str}")
        print(f"ID List {id_list}")
        return temp_str,case_history_updated,id_list  
           
            
    else:
        res2=""
        print("Case length  is Zero")
        temp_str=""
        id_list=None
        no_data_id_list=[]
        for j in qco_id_list:
            if j not in case.keys():
                no_data_id_list.append(j)
                case[j] = str(j)+ " does not exists or is invalid number"
                res2=res2+"\n\n"+case[j]
        print(f"No data ID List - {no_data_id_list}")        
        temp_str = temp_str +"\n\n"+ res2        
        case_history = case | case_history  
    
        
        return temp_str,case_history,id_list
        
    
   
    


def get_res(columns,table_name,where_clause,instance_url, access_token):
    
    query_text = "SELECT %s FROM %s WHERE %s" % (", ".join(columns), table_name, where_clause)
    if not is_valid_sql(query_text):
        print("Not a valid SQL")
        return [],[]
    
    print(f"Query is {query_text}")

    query_url = f"{instance_url}/services/data/v60.0/query/"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    params = {"q": query_text}
    response = requests.get(query_url, headers=headers, params={"q": "SELECT CaseNumber from Case"})
    if response.status_code == 200:
        return response.json().get('records', []),params
    else:
        print(f"Failed to retrieve case status. Status code: {response.status_code}")
        print(f"Error: {response.json()}")
        logging.error(f"Failed to retrieve case status. Status code: {response.status_code}")
        logging.error(f"Error: {response.json()}")
        return [],[]


case_id_list = ['01770167','01770166']
case_history = {}
instance_url = "https://eforce--test.sandbox.my.salesforce.com"
access_token = "00D3I0000000mv9!AQEAQGa2YHm3sfDHOPRozluo6kkdXL42etbAeB2ohHnpFmb60hs7Ob.QKJ8utY8j5sbflZoBmoVqXh2FNQGVTiARmZDuNEdc"
case_status_details(case_id_list,case_history,instance_url,
                        access_token)
