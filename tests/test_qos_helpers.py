from rclpy.qos import QoSProfile, QoSReliabilityPolicy  # pants: no-infer-dep

from era_5g_relay_network_application import can_be_dropped_from_qos, queue_len_from_qos

BEST_EFFORT = QoSProfile(reliability=QoSReliabilityPolicy.BEST_EFFORT, depth=1)
RELIABLE = QoSProfile(reliability=QoSReliabilityPolicy.RELIABLE, depth=10)


def test_queue_len_from_qos() -> None:
    assert queue_len_from_qos(42, None) == 42
    assert queue_len_from_qos(42, BEST_EFFORT) == 42
    assert queue_len_from_qos(42, RELIABLE) == 0


def test_can_be_dropped_from_qos() -> None:
    assert can_be_dropped_from_qos(None)
    assert can_be_dropped_from_qos(BEST_EFFORT)
    assert not can_be_dropped_from_qos(RELIABLE)
