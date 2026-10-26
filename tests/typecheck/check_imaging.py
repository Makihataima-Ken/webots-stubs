"""Type-checking tests for the camera, range-finder and lidar modules (checked by mypy and pyright, never run)."""

import ctypes
from ctypes import _Pointer  # pyright: ignore[reportPrivateUsage]

from typing_extensions import assert_type

from controller import Camera, CameraRecognitionObject, Lidar, LidarPoint, RangeFinder

# Camera
camera = Camera("camera", 32)
assert_type(camera.getImage(), bytes)
assert_type(camera.image, bytes)
assert_type(camera.getImageArray(), list[list[list[int]]] | None)
assert_type(camera.getWidth(), int)
assert_type(camera.fov, float)
assert_type(camera.saveImage("image.png", 100), int)
assert_type(Camera.imageGetRed(camera.getImage(), camera.getWidth(), 0, 0), int)
assert_type(Camera.imageGetGreen(camera.getImage(), camera.getWidth(), 0, 0), int)
assert_type(Camera.imageGetBlue(camera.getImage(), camera.getWidth(), 0, 0), int)
assert_type(Camera.imageGetGray(camera.getImage(), camera.getWidth(), 0, 0), float)

camera.fov = 0.5
camera.exposure = 1.5
camera.focal_distance = 2.0
camera.setFov(0.5)
camera.setExposure(1.0)
camera.setFocalDistance(1.0)

# Recognition
assert_type(camera.hasRecognition(), bool)
camera.recognitionEnable(64)
camera.enableRecognitionSegmentation()
assert_type(camera.getRecognitionSegmentationImage(), bytes)
assert_type(camera.segmentation_image, bytes)
assert_type(camera.getRecognitionSegmentationImageArray(), list[list[list[int]]] | None)
assert_type(camera.saveRecognitionSegmentationImage("seg.png", 90), int)

objects = camera.getRecognitionObjects()
assert_type(objects, list[CameraRecognitionObject])
for obj in objects:
    assert_type(obj.getId(), int)
    assert_type(obj.id, int)
    assert_type(obj.getPosition(), ctypes.Array[ctypes.c_double])
    assert_type(obj.getPositionOnImage(), ctypes.Array[ctypes.c_int])
    assert_type(obj.getColors(), _Pointer[ctypes.c_double])
    assert_type(obj.getModel(), str)
    assert_type(obj.model, str)

# RangeFinder
finder = RangeFinder("range-finder")
assert_type(finder.getRangeImage(), list[float])
assert_type(finder.getRangeImage("list"), list[float])
assert_type(finder.getRangeImage(data_type="list"), list[float])
assert_type(finder.getRangeImage("buffer"), _Pointer[ctypes.c_float])
assert_type(finder.getRangeImage(data_type="buffer"), _Pointer[ctypes.c_float])
assert_type(finder.range_image, _Pointer[ctypes.c_float])
assert_type(finder.getRangeImageArray(), list[list[float]])
assert_type(RangeFinder.rangeImageGetDepth(finder.getRangeImage(), finder.getWidth(), 1, 2), float)
assert_type(RangeFinder.rangeImageGetDepth(finder.range_image, finder.getWidth(), 1, 2), float)
assert_type(finder.getMaxRange(), float)
assert_type(finder.max_range, float)
assert_type(finder.width, int)
assert_type(finder.saveImage("depth.hdr", 100), int)


def range_image(data_type: str) -> None:
    # A data_type only known as a str gives either result.
    assert_type(finder.getRangeImage(data_type), list[float] | _Pointer[ctypes.c_float])


# Lidar
lidar = Lidar("lidar")
assert_type(lidar.getRangeImage(), list[float])
assert_type(lidar.getRangeImageArray(), list[list[float]])
assert_type(lidar.getLayerRangeImage(0), list[float])
assert_type(lidar.range_image, _Pointer[ctypes.c_float])
assert_type(lidar.getFrequency(), float)
assert_type(lidar.frequency, float)
assert_type(lidar.number_of_layers, int)
assert_type(lidar.getNumberOfPoints(), int)
assert_type(lidar.isPointCloudEnabled(), bool)

lidar.frequency = 10.0
lidar.setFrequency(10.0)
lidar.enablePointCloud()
lidar.disablePointCloud()

cloud = lidar.getPointCloud()
assert_type(cloud, list[LidarPoint])
assert_type(lidar.getLayerPointCloud(1), list[LidarPoint])

# LidarPoint
point = cloud[0]
assert_type(point.x, float)
assert_type(point.y, float)
assert_type(point.z, float)
assert_type(point.layer, int)
assert_type(point.time, float)
assert_type(LidarPoint(b"\x00" * 20, 0), LidarPoint)
