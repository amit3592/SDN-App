
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h2' )
        rightHost = self.addHost( 'h3' )
        centerHost = self.addHost( 'h4' )

        rightSwitch = self.addSwitch( 's1' )

        # Add links
        self.addLink( leftHost, rightSwitch )
        self.addLink( rightHost, rightSwitch )
        self.addLink(  centerHost, rightSwitch )


topos = { 'mytopo': ( lambda: MyTopo() ) }

