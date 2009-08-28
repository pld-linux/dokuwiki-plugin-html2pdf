# TODO
# - use more system pkgs
%define		plugin		html2pdf
Summary:	DokuWiki plugin to export HTML to PDF
Summary(pl.UTF-8):	Wtyczka html2pdf dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20090215
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://snorriheim.dnsdojo.com/dokuPlugins/html2pdf.tar.gz
# Source0-md5:	89e8a250bbb14f0ce9d649c286a415b4
URL:		http://wiki.splitbrain.org/plugin:html2pdf
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
DokuWiki plugin to export HTML to PDF.

%description -l pl.UTF-8
Wtyczka dla DokuWiki

%prep
%setup -q -n %{plugin}
%{__sed} -i -e 's,\r$,,' info.txt
version=$(awk '/date/{print $2}' info.txt)
if [ $(echo "$version" | tr -d -) != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a action.php conf $RPM_BUILD_ROOT%{plugindir}
cp -a html2ps $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/conf
%{plugindir}/html2ps
