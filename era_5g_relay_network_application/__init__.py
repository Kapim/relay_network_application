from multiprocessing.queues import Queue as MpQueue
from queue import Queue
from typing import Any, Optional, Protocol, Union

from rclpy.qos import QoSProfile, QoSReliabilityPolicy  # pants: no-infer-dep

AnyQueue = Union[Queue, MpQueue]


class SendFunctionProtocol(Protocol):
    # Define types here, as if __call__ were a function (ignore self).
    def __call__(self, data: Any, sid: Optional[str] = None) -> None:
        ...


def can_be_dropped_from_qos(qos: Optional[QoSProfile] = None) -> bool:
    if qos is None:
        return True

    is_best_effort = qos.reliability == QoSReliabilityPolicy.BEST_EFFORT
    assert isinstance(is_best_effort, bool)  # this is necessary for mypy
    return is_best_effort


def queue_len_from_qos(default_len: int, qos: Optional[QoSProfile] = None) -> int:
    return default_len if qos is None or qos.reliability == QoSReliabilityPolicy.BEST_EFFORT else 0
