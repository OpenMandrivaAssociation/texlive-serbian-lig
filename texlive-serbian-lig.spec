Name:		texlive-serbian-lig
Version:	53127
Release:	2
Summary:	Control ligatures in Serbian
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/serbian-lig
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-lig.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-lig.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
