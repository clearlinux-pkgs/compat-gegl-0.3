#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-gegl-0.3
Version  : 0.3.28
Release  : 1
URL      : https://download.gimp.org/pub/gegl/0.3/gegl-0.3.28.tar.bz2
Source0  : https://download.gimp.org/pub/gegl/0.3/gegl-0.3.28.tar.bz2
Summary  : Generic Graphics Library
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0 LGPL-3.0
Requires: compat-gegl-0.3-bin
Requires: compat-gegl-0.3-lib
Requires: compat-gegl-0.3-data
Requires: compat-gegl-0.3-locales
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : graphviz
BuildRequires : lcms2-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(babl)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(exiv2)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gexiv2)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(lensfun)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libraw)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libv4l2)
BuildRequires : pkgconfig(lua)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(pygobject-3.0)
BuildRequires : python
BuildRequires : ruby-dev

%description
GEGL-0.3.28
GEGL
GEGL
GEGL (Generic Graphics Library) is a data flow based image processing
framework, providing floating point processing and non-destructive
image processing capabilities to GNU Image Manipulation Program and
other projects (imgflo, GNOME Photos, gcut, iconographer, â¦)

%package bin
Summary: bin components for the compat-gegl-0.3 package.
Group: Binaries
Requires: compat-gegl-0.3-data

%description bin
bin components for the compat-gegl-0.3 package.


%package data
Summary: data components for the compat-gegl-0.3 package.
Group: Data

%description data
data components for the compat-gegl-0.3 package.


%package dev
Summary: dev components for the compat-gegl-0.3 package.
Group: Development
Requires: compat-gegl-0.3-lib
Requires: compat-gegl-0.3-bin
Requires: compat-gegl-0.3-data
Provides: compat-gegl-0.3-devel

%description dev
dev components for the compat-gegl-0.3 package.


%package lib
Summary: lib components for the compat-gegl-0.3 package.
Group: Libraries
Requires: compat-gegl-0.3-data

%description lib
lib components for the compat-gegl-0.3 package.


%package locales
Summary: locales components for the compat-gegl-0.3 package.
Group: Default

%description locales
locales components for the compat-gegl-0.3 package.


%prep
%setup -q -n gegl-0.3.28

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1524857830
%configure --disable-static --without-jasper --without-tiff --disable-docs PYTHON=/usr/bin/python3 --without-vala
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1524857830
rm -rf %{buildroot}
%make_install
%find_lang gegl-0.3

%files
%defattr(-,root,root,-)
/usr/lib64/gegl-0.3/grey2.json

%files bin
%defattr(-,root,root,-)
/usr/bin/gcut
/usr/bin/gegl
/usr/bin/gegl-imgcmp

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Gegl-0.3.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/gegl-0.3/gegl-apply.h
/usr/include/gegl-0.3/gegl-audio-fragment.h
/usr/include/gegl-0.3/gegl-buffer-backend.h
/usr/include/gegl-0.3/gegl-buffer-cl-iterator.h
/usr/include/gegl-0.3/gegl-buffer-iterator.h
/usr/include/gegl-0.3/gegl-buffer.h
/usr/include/gegl-0.3/gegl-color.h
/usr/include/gegl-0.3/gegl-cpuaccel.h
/usr/include/gegl-0.3/gegl-curve.h
/usr/include/gegl-0.3/gegl-debug.h
/usr/include/gegl-0.3/gegl-enums.h
/usr/include/gegl-0.3/gegl-graph-debug.h
/usr/include/gegl-0.3/gegl-init.h
/usr/include/gegl-0.3/gegl-lookup.h
/usr/include/gegl-0.3/gegl-matrix.h
/usr/include/gegl-0.3/gegl-node.h
/usr/include/gegl-0.3/gegl-op.h
/usr/include/gegl-0.3/gegl-operations-util.h
/usr/include/gegl-0.3/gegl-paramspecs.h
/usr/include/gegl-0.3/gegl-path.h
/usr/include/gegl-0.3/gegl-plugin.h
/usr/include/gegl-0.3/gegl-processor.h
/usr/include/gegl-0.3/gegl-random.h
/usr/include/gegl-0.3/gegl-tile-backend.h
/usr/include/gegl-0.3/gegl-tile-handler.h
/usr/include/gegl-0.3/gegl-tile-source.h
/usr/include/gegl-0.3/gegl-tile.h
/usr/include/gegl-0.3/gegl-types.h
/usr/include/gegl-0.3/gegl-utils.h
/usr/include/gegl-0.3/gegl-version.h
/usr/include/gegl-0.3/gegl.h
/usr/include/gegl-0.3/npd/deformation.h
/usr/include/gegl-0.3/npd/graphics.h
/usr/include/gegl-0.3/npd/lattice_cut.h
/usr/include/gegl-0.3/npd/npd.h
/usr/include/gegl-0.3/npd/npd_common.h
/usr/include/gegl-0.3/npd/npd_debug.h
/usr/include/gegl-0.3/npd/npd_gegl.h
/usr/include/gegl-0.3/npd/npd_math.h
/usr/include/gegl-0.3/opencl/cl.h
/usr/include/gegl-0.3/opencl/cl_d3d10.h
/usr/include/gegl-0.3/opencl/cl_ext.h
/usr/include/gegl-0.3/opencl/cl_gl.h
/usr/include/gegl-0.3/opencl/cl_gl_ext.h
/usr/include/gegl-0.3/opencl/cl_platform.h
/usr/include/gegl-0.3/opencl/gegl-cl-color.h
/usr/include/gegl-0.3/opencl/gegl-cl-init.h
/usr/include/gegl-0.3/opencl/gegl-cl-random.h
/usr/include/gegl-0.3/opencl/gegl-cl-types.h
/usr/include/gegl-0.3/opencl/gegl-cl.h
/usr/include/gegl-0.3/opencl/opencl.h
/usr/include/gegl-0.3/operation/gegl-extension-handler.h
/usr/include/gegl-0.3/operation/gegl-operation-area-filter.h
/usr/include/gegl-0.3/operation/gegl-operation-composer.h
/usr/include/gegl-0.3/operation/gegl-operation-composer3.h
/usr/include/gegl-0.3/operation/gegl-operation-context.h
/usr/include/gegl-0.3/operation/gegl-operation-filter.h
/usr/include/gegl-0.3/operation/gegl-operation-handlers.h
/usr/include/gegl-0.3/operation/gegl-operation-meta-json.h
/usr/include/gegl-0.3/operation/gegl-operation-meta.h
/usr/include/gegl-0.3/operation/gegl-operation-point-composer.h
/usr/include/gegl-0.3/operation/gegl-operation-point-composer3.h
/usr/include/gegl-0.3/operation/gegl-operation-point-filter.h
/usr/include/gegl-0.3/operation/gegl-operation-point-render.h
/usr/include/gegl-0.3/operation/gegl-operation-property-keys.h
/usr/include/gegl-0.3/operation/gegl-operation-sink.h
/usr/include/gegl-0.3/operation/gegl-operation-source.h
/usr/include/gegl-0.3/operation/gegl-operation-temporal.h
/usr/include/gegl-0.3/operation/gegl-operation.h
/usr/include/gegl-0.3/sc/sc-common.h
/usr/include/gegl-0.3/sc/sc-context.h
/usr/include/gegl-0.3/sc/sc-outline.h
/usr/include/gegl-0.3/sc/sc-sample.h
/usr/lib64/libgegl-0.3.so
/usr/lib64/libgegl-npd-0.3.so
/usr/lib64/libgegl-sc-0.3.so
/usr/lib64/pkgconfig/gegl-0.3.pc
/usr/lib64/pkgconfig/gegl-sc-0.3.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/gegl-0.3/gegl-common-gpl3.so
/usr/lib64/gegl-0.3/gegl-common.so
/usr/lib64/gegl-0.3/gegl-core.so
/usr/lib64/gegl-0.3/gegl-generated.so
/usr/lib64/gegl-0.3/jpg-load.so
/usr/lib64/gegl-0.3/jpg-save.so
/usr/lib64/gegl-0.3/lcms-from-profile.so
/usr/lib64/gegl-0.3/npd.so
/usr/lib64/gegl-0.3/npy-save.so
/usr/lib64/gegl-0.3/path.so
/usr/lib64/gegl-0.3/pixbuf.so
/usr/lib64/gegl-0.3/png-load.so
/usr/lib64/gegl-0.3/png-save.so
/usr/lib64/gegl-0.3/ppm-load.so
/usr/lib64/gegl-0.3/ppm-save.so
/usr/lib64/gegl-0.3/raw-load.so
/usr/lib64/gegl-0.3/rgbe-load.so
/usr/lib64/gegl-0.3/rgbe-save.so
/usr/lib64/gegl-0.3/save-pixbuf.so
/usr/lib64/gegl-0.3/seamless-clone-compose.so
/usr/lib64/gegl-0.3/seamless-clone.so
/usr/lib64/gegl-0.3/svg-load.so
/usr/lib64/gegl-0.3/text.so
/usr/lib64/gegl-0.3/transformops.so
/usr/lib64/gegl-0.3/v4l.so
/usr/lib64/gegl-0.3/vector-fill.so
/usr/lib64/gegl-0.3/vector-stroke.so
/usr/lib64/libgegl-0.3.so.0
/usr/lib64/libgegl-0.3.so.0.328.0

%files locales -f gegl-0.3.lang
%defattr(-,root,root,-)

