with open("/root/ip", "r") as ip_file:
    ip = ip_file.readline().strip()

data = """
<?xml version="1.0"?>
<TradeServerInstanceSettings xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <ForcePriceServer />
  <RelayServerURL />
  <RelaySecret1 />
  <RelaySecret2 />
  <IsBetaTester>false</IsBetaTester>
  <RunAtLowPower>false</RunAtLowPower>
  <BackTestingPriceType>0</BackTestingPriceType>
  <BackTestingReportAction>0</BackTestingReportAction>
  <BetaReportEmailAdres />
  <LastBetaVersionCheck>2018-04-07T21:24:23.078154Z</LastBetaVersionCheck>
  <ExecuteEncryptProcedure>false</ExecuteEncryptProcedure>
  <ReallyExecuteEncryptProcedure>true</ReallyExecuteEncryptProcedure>
  <Username>D41D8CD98F00B204E9800998ECF8427E</Username>
  <Password>D41D8CD98F00B204E9800998ECF8427E</Password>
  <OpenInterfaceOnStartup>false</OpenInterfaceOnStartup>
  <HaasbotEnabledOnStartup>false</HaasbotEnabledOnStartup>
  <BotsEnabledOnStartup>false</BotsEnabledOnStartup>
  <HostingAdres>{ip}</HostingAdres>
  <ExternalAdres />
  <HostingPort>8090</HostingPort>
  <HubPort>8092</HubPort>
  <TFAEnabled>false</TFAEnabled>
  <LocalAPIAdres />
  <LocalAPIPort>0</LocalAPIPort>
  <LocalAPIToken />
  <AutoLogOutMinutes>10</AutoLogOutMinutes>
  <MaxMonthsBack>12</MaxMonthsBack>
</TradeServerInstanceSettings>
""".format(ip=ip)

with open("/root/HTS/Settings/MainSettings.XML", "w") as settings_file:
    settings_file.write(data)

print ("IP: ", ip)
