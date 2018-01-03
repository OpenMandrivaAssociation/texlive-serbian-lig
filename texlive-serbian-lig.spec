Name:		texlive-serbian-lig
Version:	20170414
Release:	1
Summary:	Control ligatures in Serbian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/serbian-lig
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-lig.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-lig.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package suppresses fi and fl (and other ligatures) in
Serbian text written using Roman script.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/serbian-lig
%doc %{_texmfdistdir}/doc/latex/serbian-lig

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
