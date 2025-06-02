import re

SQL_REGEX = re.compile(
    r"""^
    SELECT\s+
    (?P<columns>
        [a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)?
        (\s*,\s*[a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)?)*
    )
    \s+FROM\s+Case\s+WHERE\s+
    CaseNumber\s+IN\s+\(\s*'[^']*'(\s*,\s*'[^']*')*\s*\)\s+OR\s+
    ECS_Quote__r\.Quote_Number__c\s+IN\s+\(\s*'[^']*'(\s*,\s*'[^']*')*\s*\)\s+OR\s+
    AE_CM_Order__r\.Name\s+IN\s+\(\s*'[^']*'(\s*,\s*'[^']*')*\s*\)\s+OR\s+
    AE_CM_Invoice__r\.Name\s+IN\s+\(\s*'[^']*'(\s*,\s*'[^']*')*\s*\)\s+OR\s+
    AE_CM_Order__r\.AE_Partner_PO__c\s+IN\s+\(\s*'[^']*'(\s*,\s*'[^']*')*\s*\)
    $
    """,
    re.IGNORECASE | re.VERBOSE
)



def is_valid_sql(query: str) -> bool:
    query = query.strip()
    if not query.lower().startswith("select") or " from case where " not in query.lower():
        return False
    return SQL_REGEX.match(query.strip()) is not None

