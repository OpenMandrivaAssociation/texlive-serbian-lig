%global tl_name serbian-lig
%global tl_revision 53127

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Control ligatures in Serbian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/serbian/filipovic/serbian-lig
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-lig.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/serbian-lig.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package suppresses fi and fl (and other ligatures) in Serbian text
written using Roman script.

