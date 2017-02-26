# check-mk_signal-cli
Send check_mk notifications via signal-cli (requires https://github.com/AsamK/signal-cli)

Store script at /omd/sites/\<YOUR-SITE\>/share/check_mk/notifications

Adjust \<SIGNAL-CLI-PATH\>, \<USER-SENDER\>, and \<USER-RECEIVER\>

Integrate at WATO / Notifications, select Notification Method "Send via Signal"

Messages will look like:
\<HOSTNAME\>: \<NEW-HOSTSTATE\> after \<OLD-HOSTSTATE\> (\<OLD-STATE-DURATION\>) at \<LONG-DATE-TIME\>
