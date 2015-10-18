if ADD_SYSTEMD
EXTRA_DIST = udevil.conf devmon devmon@.service
else
EXTRA_DIST = udevil.conf
endif

install-data-hook:
	test -d $(DESTDIR)/$(sysconfdir)/udevil || mkdir -p -- \
				$(DESTDIR)/$(sysconfdir)/udevil
	test -f $(DESTDIR)/$(sysconfdir)/udevil/udevil.conf || $(INSTALL_DATA) \
				$(srcdir)/udevil.conf \
				$(DESTDIR)/$(sysconfdir)/udevil/udevil.conf
if ADD_SYSTEMD
	test -d $(DESTDIR)/etc/sysconfig || mkdir -p -- $(DESTDIR)/etc/sysconfig
	test -f $(DESTDIR)/etc/sysconfig/devmon || $(INSTALL_DATA) \
				$(srcdir)/systemd/devmon $(DESTDIR)/etc/sysconfig/devmon
	test -d $(DESTDIR)/lib/systemd/system || \
				mkdir -p -- $(DESTDIR)/lib/systemd/system
	$(INSTALL_DATA) $(srcdir)/systemd/devmon@.service \
				$(DESTDIR)/lib/systemd/system/devmon@.service
endif
