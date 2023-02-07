# Be sure to export your API key first from the shell
# Do not put it in source code
# API_KEY=ehg549g5hilull4w7985go
# refer to https://developer.cisco.com/meraki/api-latest/
import meraki
dashboard = meraki.DashboardAPI(API_KEY)
my_orgs = dashboard.organizations.getOrganizations()
