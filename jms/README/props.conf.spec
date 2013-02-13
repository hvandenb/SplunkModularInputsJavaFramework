# --------------------------------------------------------
# Props Examples
#  These are examples as to how you can handle some of the
#  JMS inputs
# --------------------------------------------------------

#[<spec>]

#LINE_BREAKER = ([\r\n]+(?=(\w+ \w+ \d{2}\s\d{2}:\d{2}:\d{2} \w+ \d{4})))

#
# Using the JMSTimestamp as the event time
# NOTE: A JMS sender can disable setting this so be aware that you might not get this
#

# TIME_PREFIX= msg_header_timestamp="
# TIME_FORMAT= %s
# MAX_TIMESTAMP_LOOKAHEAD = 30