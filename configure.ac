AC_PREREQ([2.72])
AC_INIT([garagejam],[5.0.0],[ole@aamot.org])
AM_INIT_AUTOMAKE([-Wno-portability 1.11 no-dist-gzip dist-xz tar-ustar subdir-objects])
AM_MAINTAINER_MODE
AC_CONFIG_SRCDIR([src/garagejam-gingerblue-main.c])
AC_CONFIG_HEADERS([config.h])
AC_PROG_CC

# ***********
# Translation
# ***********

AM_GLIB_GNU_GETTEXT
IT_PROG_INTLTOOL([0.50.1])

GETTEXT_PACKAGE=AC_PACKAGE_NAME
AC_SUBST(GETTEXT_PACKAGE)
AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE, "$GETTEXT_PACKAGE", [Gettext package.])

PKG_CHECK_MODULES(GARAGEJAM,
                  glib-2.0 >= 2.38.0 \
                  gobject-2.0 >= 2.38.0 \
                  gstreamer-1.0 >= 1.0 \
		  gstreamer-player-1.0 >= 1.0 \
		  gstreamer-plugins-bad-1.0 \
                  gstreamer-plugins-base-1.0 \
		  gstreamer-tag-1.0 >= 1.0 \
                  gstreamer-video-1.0 \
                  gtk+-3.0 >= 3.24.23 \
                  libxml-2.0 >= 2.0 \
                  pangoft2 >= 0.28)
GARAGEJAM_PKG_DEPS="glib-1.0 gobject-2.0 gstreamer-1.0 gstreamer-player-1.0 gstreamer-plugins-bad-1.0 gstreamer-plugins-base-1.0 gstreamer-tag-1.0 gstreamer-video-1.0 gtk+-3.0 libxml-2.0 pangoft2"

AC_SUBST(GARAGEJAM_LIBS)
AC_SUBST(GARAGEJAM_CFLAGS)
AC_SUBST(GARAGEJAM_PKG_DEPS)

AC_CONFIG_FILES([
Makefile
garagejam.spec
data/Makefile
data/garagejam.appdata.xml
data/garagejam.desktop.in
data/icons/Makefile
po/Makefile.in
src/Makefile
src/garagejam.xml
])
AC_OUTPUT
