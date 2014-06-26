from __future__ import absolute_import

try:
    from schematics.models import Model as SchematicsSerializer
except ImportError:
    SchematicsSerializer = None

try:
    from marshmallow import Serializer as MarshmallowSerializer
except ImportError:
    MarshmallowSerializer = None


def adapter_for(serializer):
    if isinstance(serializer(), SchematicsSerializer):
        from hyp.adapters.schematics import Adapter as SchematicsAdapter
        return SchematicsAdapter
    elif isinstance(serializer(), MarshmallowSerializer):
        from hyp.adapters.marshmallow import Adapter as MarshmallowAdapter
        return MarshmallowAdapter
    else:
        raise NotImplementedError()
