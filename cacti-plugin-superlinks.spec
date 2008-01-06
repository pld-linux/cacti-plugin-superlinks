%define		namesrc	superlinks
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - SuperLinks
Summary(pl.UTF-8):	Wtyczka do Cacti - SuperLinks
Name:		cacti-plugin-superlinks
Version:	0.71
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://wotsit.thingy.com/haj/cacti/%{namesrc}-%{version}.zip
# Source0-md5:	2fe58f1fe66071c90b2c4a9a68ed8fdb
URL:		http://wotsit.thingy.com/haj/cacti/superlinks-plugin.html
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
This is a plugin for the Cacti Plugin Architecture created by Jimmy
Conner for Cacti 0.8.x (0.9.0 is slated to have a new plugin system
from the start). It it lets you have any number of pages of arbitrary
HTML content behind tabs at the top of the page or extra entries on
the Console menu. You could use this to integrate other tools into
Cacti - say you want to have links to Smokeping, or Request Tracker,
or Nagios...

It is intended as a replacement for the Links plugin that I wrote some
time ago, but with the following key improvements:

- Any number of tabs/menu items
- For tabs, a Cacti-style tab image is generated, so your additional
  pages are integrated into Cacti better
- It uses Weathermap's access-control code, so you can make tabs that
  are only visible to certain users
- In addition to tabs, there is the option to make Console Menu items,
  and 'Welcome Page' items.
- You can embed an external webpage directly, without writing any
  HTML, if that's all you need.

%description -l pl.UTF-8
To jest bardzo prosta wtyczka dla architektury wtyczek Cacti
stworzonej przez Jimmy'ego Smitha dla Cacti 0.8.x (0.9.0 ma mieć nowy
system wtyczek). Pozwala podpiąć dowolną liczbę stron HTML dowolnej
treści pod zakładki na górnej części strony lub jako dodatkowe wpisy
w menu Console. Wtyczki tej można używać do integracji innych narzędzi
w Cacti - w ten sposób można mieć w Cacti odnośniki do Smokepinga,
Request Trackera czy Nagiosa.

Wtyczka ma zastąpić wtyczkę Links tego samego autora, napisaną
wcześniej; ma następujące rozszerzenia:
- dowolną liczbę elementów zakładek/menu
- dla zakładek generowany jest obrazek w stylu Cacti, więc dodatkowe
  strony lepiej integrują się z Cacti
- wykorzystuje kod kontroli dostępu z Weathermap, więc zakładki mogą
  być widoczne tylko dla wybranych użytkowników
- oprócz zakładek jest możliwość tworzenia elementów menu Console oraz
  strony powitalnej
- można osadzać zewnętrzne strony bezpośrednio, bez pisania
  jakiegokolwiek HTML-a.

%prep
%setup -q -n %{namesrc}
# undos the source
find '(' -name '*.php' -o -name '*.inc' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -a * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{webcactipluginroot}
