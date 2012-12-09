# revision 19440
# category Package
# catalog-ctan /macros/generic/diagrams/dcpic
# catalog-date 2009-12-22 14:54:36 +0100
# catalog-license lppl
# catalog-version 4.3.2
Name:		texlive-dcpic
Version:	4.3.2
Release:	2
Summary:	Commutative diagrams in a LaTeX and TeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/diagrams/dcpic
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dcpic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dcpic.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
DCpic is a package for typesetting Commutative Diagrams within
a LaTeX and TeX documents. Its distinguishing features are: a
powerful graphical engine, the PiCTeX package; an easy
specification syntax in which a commutative diagram is
described in terms of its objects and its arrows (morphism),
positioned in a Cartesian coordinate system.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/dcpic/dcpic.sty
%doc %{_texmfdistdir}/doc/generic/dcpic/README
%doc %{_texmfdistdir}/doc/generic/dcpic/README.TEXLIVE
%doc %{_texmfdistdir}/doc/generic/dcpic/examples.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.3.2-2
+ Revision: 750879
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.3.2-1
+ Revision: 718208
- texlive-dcpic
- texlive-dcpic
- texlive-dcpic
- texlive-dcpic

