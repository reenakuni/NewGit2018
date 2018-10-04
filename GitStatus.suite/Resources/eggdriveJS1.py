import xmlrpclib

#import xmlrpclib

#import xmlrpclib

# connect to eggPlant instance
server = xmlrpclib.ServerProxy("http://127.0.0.1:5400")


# Start the session
server.startsession("/Users/jeanette/Documents/eggDriveTests.suite")

# Verify that you can pass suiteinfo() without an argument in drive mode

# Failed before 
try:
   server.execute("put suiteinfo()")
except:
   server.endsession("")

# Worked before
# server.execute("put suiteinfo(\"/Users/jeanette/Documents/TestProjects/ePF/CornerStoneWorkingCopy/Jeannette/testsuites_no_scm/eggDriveTests.suite\")")


server.endsession("")
