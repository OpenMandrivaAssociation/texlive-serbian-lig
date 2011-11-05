# revision 23382
# category Package
# catalog-ctan /macros/latex/contrib/serbian-lig
# catalog-date 2011-07-03 09:55:42 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-serbian-lig
Version:	20110703
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package suppresses fi and fl (and other ligatures) in
Serbian text written using Roman script.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/serbian-lig/serbian-lig.sty
%doc %{_texmfdistdir}/doc/latex/serbian-lig/README
%doc %{_texmfdistdir}/doc/latex/serbian-lig/lig-list.pdf
%doc %{_texmfdistdir}/doc/latex/serbian-lig/lig-list.tex
%doc %{_texmfdistdir}/doc/latex/serbian-lig/serbian-lig.pdf
%doc %{_texmfdistdir}/doc/latex/serbian-lig/serbian-lig.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
