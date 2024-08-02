pkgbase=ocean
pkgname=(ocean)
pkgver=2.9.0-rc2
_dirver=$(echo $pkgver | cut -d. -f1-3)
pkgrel=1
arch=(x86_64)
pkgdesc='Artwork, styles and assets for the Ocean visual style for the Lingmo OS'
url='https://github.com/LingmoOS/lingmo-ocean'
license=(LGPL-2.0-or-later)
depends=(ocean-icons
         frameworkintegration
         gcc-libs
         glibc
         kcmutils
         kcolorscheme
         kconfig
         kcoreaddons
         kdecoration
         kguiaddons
         ki18n
         kiconthemes
         kirigami
         kwidgetsaddons
         kwindowsystem
         qt6-base
         qt6-declarative)
makedepends=(extra-cmake-modules
             frameworkintegration5
             kconfigwidgets5
             kiconthemes5
             lingmoui
             kwindowsystem5)
optdepends=('ocean-gtk: Ocean widget style for GTK applications')
groups=(lingmo)
source=(git+$url)
sha256sums=('SKIP')
validpgpkeys=('41EF7182553A87AC18196A77F27F2FDA54F067D8') # Lingmo OS Team <team@lingmo.org>

build() {
  cmake -B build -S lingmo-$pkgname \
    -DBUILD_TESTING=OFF \
    -DBUILD_QT5=OFF
  cmake --build build
}

package_ocean() {
  DESTDIR="$pkgdir" cmake --install build
}
