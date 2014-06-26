from __future__ import absolute_import

def adapter_for(serializer):
    from schematics.models import Model as SchematicsSerializer
    from marshmallow import Serializer as MarshmallowSerializer

    from hyp.adapters.schematics import Adapter as SchematicsAdapter
    from hyp.adapters.marshmallow import Adapter as MarshmallowAdapter

    if isinstance(serializer(), SchematicsSerializer):
        return SchematicsAdapter
    elif isinstance(serializer(), MarshmallowSerializer):
        return MarshmallowAdapter
    else:
        raise NotImplementedError()
