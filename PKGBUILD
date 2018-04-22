# Script generated with Bloom
pkgdesc="ROS - A ROS driver for OpenNI depth (+ RGB) cameras. These include: Microsoft Kinect, PrimeSense PSDK, ASUS Xtion Pro and Pro Live The driver publishes raw depth, RGB, and IR image streams."
url='http://www.ros.org/wiki/openni_camera'

pkgname='ros-lunar-openni-camera'
pkgver='1.10.0_0'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('libusbx'
'log4cxx'
'openni'
'ros-lunar-camera-info-manager'
'ros-lunar-catkin'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-image-transport'
'ros-lunar-nodelet'
'ros-lunar-roscpp'
'ros-lunar-sensor-msgs'
)

depends=('libusbx'
'log4cxx'
'openni'
'ros-lunar-camera-info-manager'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-image-transport'
'ros-lunar-nodelet'
'ros-lunar-roscpp'
'ros-lunar-sensor-msgs'
)

conflicts=()
replaces=()

_dir=openni_camera
source=()
md5sums=()

prepare() {
    cp -R $startdir/openni_camera $srcdir/openni_camera
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

