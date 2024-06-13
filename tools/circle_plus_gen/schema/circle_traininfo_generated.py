# generated based on commit(b3ff53668e165843d99a108d16ab14bc2cfca669)
# automatically generated by the FlatBuffers compiler, do not modify

# namespace: circle

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()


class Optimizer(object):
    SGD = 0
    ADAM = 1


class OptimizerOptions(object):
    NONE = 0
    SGDOptions = 1
    AdamOptions = 2


def OptimizerOptionsCreator(unionType, table):
    from flatbuffers.table import Table
    if not isinstance(table, Table):
        return None
    if unionType == OptimizerOptions().SGDOptions:
        return SGDOptionsT.InitFromBuf(table.Bytes, table.Pos)
    if unionType == OptimizerOptions().AdamOptions:
        return AdamOptionsT.InitFromBuf(table.Bytes, table.Pos)
    return None


class LossFn(object):
    SPARSE_CATEGORICAL_CROSSENTROPY = 0
    CATEGORICAL_CROSSENTROPY = 1
    MEAN_SQUARED_ERROR = 2


class LossFnOptions(object):
    NONE = 0
    SparseCategoricalCrossentropyOptions = 1
    CategoricalCrossentropyOptions = 2
    MeanSquaredErrorOptions = 3


def LossFnOptionsCreator(unionType, table):
    from flatbuffers.table import Table
    if not isinstance(table, Table):
        return None
    if unionType == LossFnOptions().SparseCategoricalCrossentropyOptions:
        return SparseCategoricalCrossentropyOptionsT.InitFromBuf(table.Bytes, table.Pos)
    if unionType == LossFnOptions().CategoricalCrossentropyOptions:
        return CategoricalCrossentropyOptionsT.InitFromBuf(table.Bytes, table.Pos)
    if unionType == LossFnOptions().MeanSquaredErrorOptions:
        return MeanSquaredErrorOptionsT.InitFromBuf(table.Bytes, table.Pos)
    return None


class LossReductionType(object):
    SumOverBatchSize = 0
    Sum = 1


class SGDOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SGDOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsSGDOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    @classmethod
    def SGDOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x43\x54\x52\x30", size_prefixed=size_prefixed)

    # SGDOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SGDOptions
    def LearningRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0


def SGDOptionsStart(builder):
    builder.StartObject(1)


def SGDOptionsAddLearningRate(builder, learningRate):
    builder.PrependFloat32Slot(0, learningRate, 0.0)


def SGDOptionsEnd(builder):
    return builder.EndObject()


class SGDOptionsT(object):

    # SGDOptionsT
    def __init__(self):
        self.learningRate = 0.0  # type: float

    @classmethod
    def InitFromBuf(cls, buf, pos):
        sgdoptions = SGDOptions()
        sgdoptions.Init(buf, pos)
        return cls.InitFromObj(sgdoptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos + n)

    @classmethod
    def InitFromObj(cls, sgdoptions):
        x = SGDOptionsT()
        x._UnPack(sgdoptions)
        return x

    # SGDOptionsT
    def _UnPack(self, sgdoptions):
        if sgdoptions is None:
            return
        self.learningRate = sgdoptions.LearningRate()

    # SGDOptionsT
    def Pack(self, builder):
        SGDOptionsStart(builder)
        SGDOptionsAddLearningRate(builder, self.learningRate)
        sgdoptions = SGDOptionsEnd(builder)
        return sgdoptions


class AdamOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AdamOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsAdamOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    @classmethod
    def AdamOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x43\x54\x52\x30", size_prefixed=size_prefixed)

    # AdamOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AdamOptions
    def LearningRate(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # AdamOptions
    def Beta1(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # AdamOptions
    def Beta2(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # AdamOptions
    def Epsilon(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0


def AdamOptionsStart(builder):
    builder.StartObject(4)


def AdamOptionsAddLearningRate(builder, learningRate):
    builder.PrependFloat32Slot(0, learningRate, 0.0)


def AdamOptionsAddBeta1(builder, beta1):
    builder.PrependFloat32Slot(1, beta1, 0.0)


def AdamOptionsAddBeta2(builder, beta2):
    builder.PrependFloat32Slot(2, beta2, 0.0)


def AdamOptionsAddEpsilon(builder, epsilon):
    builder.PrependFloat32Slot(3, epsilon, 0.0)


def AdamOptionsEnd(builder):
    return builder.EndObject()


class AdamOptionsT(object):

    # AdamOptionsT
    def __init__(self):
        self.learningRate = 0.0  # type: float
        self.beta1 = 0.0  # type: float
        self.beta2 = 0.0  # type: float
        self.epsilon = 0.0  # type: float

    @classmethod
    def InitFromBuf(cls, buf, pos):
        adamOptions = AdamOptions()
        adamOptions.Init(buf, pos)
        return cls.InitFromObj(adamOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos + n)

    @classmethod
    def InitFromObj(cls, adamOptions):
        x = AdamOptionsT()
        x._UnPack(adamOptions)
        return x

    # AdamOptionsT
    def _UnPack(self, adamOptions):
        if adamOptions is None:
            return
        self.learningRate = adamOptions.LearningRate()
        self.beta1 = adamOptions.Beta1()
        self.beta2 = adamOptions.Beta2()
        self.epsilon = adamOptions.Epsilon()

    # AdamOptionsT
    def Pack(self, builder):
        AdamOptionsStart(builder)
        AdamOptionsAddLearningRate(builder, self.learningRate)
        AdamOptionsAddBeta1(builder, self.beta1)
        AdamOptionsAddBeta2(builder, self.beta2)
        AdamOptionsAddEpsilon(builder, self.epsilon)
        adamOptions = AdamOptionsEnd(builder)
        return adamOptions


class SparseCategoricalCrossentropyOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SparseCategoricalCrossentropyOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsSparseCategoricalCrossentropyOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    @classmethod
    def SparseCategoricalCrossentropyOptionsBufferHasIdentifier(
            cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x43\x54\x52\x30", size_prefixed=size_prefixed)

    # SparseCategoricalCrossentropyOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SparseCategoricalCrossentropyOptions
    def FromLogits(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return bool(
                self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False


def SparseCategoricalCrossentropyOptionsStart(builder):
    builder.StartObject(1)


def SparseCategoricalCrossentropyOptionsAddFromLogits(builder, fromLogits):
    builder.PrependBoolSlot(0, fromLogits, 0)


def SparseCategoricalCrossentropyOptionsEnd(builder):
    return builder.EndObject()


class SparseCategoricalCrossentropyOptionsT(object):

    # SparseCategoricalCrossentropyOptionsT
    def __init__(self):
        self.fromLogits = False  # type: bool

    @classmethod
    def InitFromBuf(cls, buf, pos):
        sparseCategoricalCrossentropyOptions = SparseCategoricalCrossentropyOptions()
        sparseCategoricalCrossentropyOptions.Init(buf, pos)
        return cls.InitFromObj(sparseCategoricalCrossentropyOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos + n)

    @classmethod
    def InitFromObj(cls, sparseCategoricalCrossentropyOptions):
        x = SparseCategoricalCrossentropyOptionsT()
        x._UnPack(sparseCategoricalCrossentropyOptions)
        return x

    # SparseCategoricalCrossentropyOptionsT
    def _UnPack(self, sparseCategoricalCrossentropyOptions):
        if sparseCategoricalCrossentropyOptions is None:
            return
        self.fromLogits = sparseCategoricalCrossentropyOptions.FromLogits()

    # SparseCategoricalCrossentropyOptionsT
    def Pack(self, builder):
        SparseCategoricalCrossentropyOptionsStart(builder)
        SparseCategoricalCrossentropyOptionsAddFromLogits(builder, self.fromLogits)
        sparseCategoricalCrossentropyOptions = SparseCategoricalCrossentropyOptionsEnd(
            builder)
        return sparseCategoricalCrossentropyOptions


class CategoricalCrossentropyOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CategoricalCrossentropyOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCategoricalCrossentropyOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    @classmethod
    def CategoricalCrossentropyOptionsBufferHasIdentifier(cls,
                                                          buf,
                                                          offset,
                                                          size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x43\x54\x52\x30", size_prefixed=size_prefixed)

    # CategoricalCrossentropyOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CategoricalCrossentropyOptions
    def FromLogits(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return bool(
                self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False


def CategoricalCrossentropyOptionsStart(builder):
    builder.StartObject(1)


def CategoricalCrossentropyOptionsAddFromLogits(builder, fromLogits):
    builder.PrependBoolSlot(0, fromLogits, 0)


def CategoricalCrossentropyOptionsEnd(builder):
    return builder.EndObject()


class CategoricalCrossentropyOptionsT(object):

    # CategoricalCrossentropyOptionsT
    def __init__(self):
        self.fromLogits = False  # type: bool

    @classmethod
    def InitFromBuf(cls, buf, pos):
        categoricalCrossentropyOptions = CategoricalCrossentropyOptions()
        categoricalCrossentropyOptions.Init(buf, pos)
        return cls.InitFromObj(categoricalCrossentropyOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos + n)

    @classmethod
    def InitFromObj(cls, categoricalCrossentropyOptions):
        x = CategoricalCrossentropyOptionsT()
        x._UnPack(categoricalCrossentropyOptions)
        return x

    # CategoricalCrossentropyOptionsT
    def _UnPack(self, categoricalCrossentropyOptions):
        if categoricalCrossentropyOptions is None:
            return
        self.fromLogits = categoricalCrossentropyOptions.FromLogits()

    # CategoricalCrossentropyOptionsT
    def Pack(self, builder):
        CategoricalCrossentropyOptionsStart(builder)
        CategoricalCrossentropyOptionsAddFromLogits(builder, self.fromLogits)
        categoricalCrossentropyOptions = CategoricalCrossentropyOptionsEnd(builder)
        return categoricalCrossentropyOptions


class MeanSquaredErrorOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MeanSquaredErrorOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMeanSquaredErrorOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    @classmethod
    def MeanSquaredErrorOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x43\x54\x52\x30", size_prefixed=size_prefixed)

    # MeanSquaredErrorOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)


def MeanSquaredErrorOptionsStart(builder):
    builder.StartObject(0)


def MeanSquaredErrorOptionsEnd(builder):
    return builder.EndObject()


class MeanSquaredErrorOptionsT(object):

    # MeanSquaredErrorOptionsT
    def __init__(self):
        pass

    @classmethod
    def InitFromBuf(cls, buf, pos):
        meanSquaredErrorOptions = MeanSquaredErrorOptions()
        meanSquaredErrorOptions.Init(buf, pos)
        return cls.InitFromObj(meanSquaredErrorOptions)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos + n)

    @classmethod
    def InitFromObj(cls, meanSquaredErrorOptions):
        x = MeanSquaredErrorOptionsT()
        x._UnPack(meanSquaredErrorOptions)
        return x

    # MeanSquaredErrorOptionsT
    def _UnPack(self, meanSquaredErrorOptions):
        if meanSquaredErrorOptions is None:
            return

    # MeanSquaredErrorOptionsT
    def Pack(self, builder):
        MeanSquaredErrorOptionsStart(builder)
        meanSquaredErrorOptions = MeanSquaredErrorOptionsEnd(builder)
        return meanSquaredErrorOptions


class ModelTraining(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ModelTraining()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsModelTraining(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    @classmethod
    def ModelTrainingBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x43\x54\x52\x30", size_prefixed=size_prefixed)

    # ModelTraining
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ModelTraining
    def Version(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # ModelTraining
    def Optimizer(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # ModelTraining
    def OptimizerOptType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # ModelTraining
    def OptimizerOpt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # ModelTraining
    def Lossfn(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # ModelTraining
    def LossfnOptType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # ModelTraining
    def LossfnOpt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # ModelTraining
    def Epochs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ModelTraining
    def BatchSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # ModelTraining
    def LossReductionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # ModelTraining
    def TrainableOps(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Int32Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ModelTraining
    def TrainableOpsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # ModelTraining
    def TrainableOpsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ModelTraining
    def TrainableOpsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0


def ModelTrainingStart(builder):
    builder.StartObject(11)


def ModelTrainingAddVersion(builder, version):
    builder.PrependUint32Slot(0, version, 0)


def ModelTrainingAddOptimizer(builder, optimizer):
    builder.PrependInt8Slot(1, optimizer, 0)


def ModelTrainingAddOptimizerOptType(builder, optimizerOptType):
    builder.PrependUint8Slot(2, optimizerOptType, 0)


def ModelTrainingAddOptimizerOpt(builder, optimizerOpt):
    builder.PrependUOffsetTRelativeSlot(
        3, flatbuffers.number_types.UOffsetTFlags.py_type(optimizerOpt), 0)


def ModelTrainingAddLossfn(builder, lossfn):
    builder.PrependInt8Slot(4, lossfn, 0)


def ModelTrainingAddLossfnOptType(builder, lossfnOptType):
    builder.PrependUint8Slot(5, lossfnOptType, 0)


def ModelTrainingAddLossfnOpt(builder, lossfnOpt):
    builder.PrependUOffsetTRelativeSlot(
        6, flatbuffers.number_types.UOffsetTFlags.py_type(lossfnOpt), 0)


def ModelTrainingAddEpochs(builder, epochs):
    builder.PrependInt32Slot(7, epochs, 0)


def ModelTrainingAddBatchSize(builder, batchSize):
    builder.PrependInt32Slot(8, batchSize, 0)


def ModelTrainingAddLossReductionType(builder, lossReductionType):
    builder.PrependInt8Slot(9, lossReductionType, 0)


def ModelTrainingAddTrainableOps(builder, trainableOps):
    builder.PrependUOffsetTRelativeSlot(
        10, flatbuffers.number_types.UOffsetTFlags.py_type(trainableOps), 0)


def ModelTrainingStartTrainableOpsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def ModelTrainingEnd(builder):
    return builder.EndObject()


try:
    from typing import List, Union
except:
    pass


class ModelTrainingT(object):

    # ModelTrainingT
    def __init__(self):
        self.version = 0  # type: int
        self.optimizer = 0  # type: int
        self.optimizerOptType = 0  # type: int
        self.optimizerOpt = None  # type: Union[None, SGDOptionsT, AdamOptionsT]
        self.lossfn = 0  # type: int
        self.lossfnOptType = 0  # type: int
        self.lossfnOpt = None  # type: Union[None, SparseCategoricalCrossentropyOptionsT, CategoricalCrossentropyOptionsT, MeanSquaredErrorOptionsT]
        self.epochs = 0  # type: int
        self.batchSize = 0  # type: int
        self.lossReductionType = 0  # type: int
        self.trainableOps = None  # type: List[int]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        modelTraining = ModelTraining()
        modelTraining.Init(buf, pos)
        return cls.InitFromObj(modelTraining)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos + n)

    @classmethod
    def InitFromObj(cls, modelTraining):
        x = ModelTrainingT()
        x._UnPack(modelTraining)
        return x

    # ModelTrainingT
    def _UnPack(self, modelTraining):
        if modelTraining is None:
            return
        self.version = modelTraining.Version()
        self.optimizer = modelTraining.Optimizer()
        self.optimizerOptType = modelTraining.OptimizerOptType()
        self.optimizerOpt = OptimizerOptionsCreator(self.optimizerOptType,
                                                    modelTraining.OptimizerOpt())
        self.lossfn = modelTraining.Lossfn()
        self.lossfnOptType = modelTraining.LossfnOptType()
        self.lossfnOpt = LossFnOptionsCreator(self.lossfnOptType,
                                              modelTraining.LossfnOpt())
        self.epochs = modelTraining.Epochs()
        self.batchSize = modelTraining.BatchSize()
        self.lossReductionType = modelTraining.LossReductionType()
        if not modelTraining.TrainableOpsIsNone():
            if np is None:
                self.trainableOps = []
                for i in range(modelTraining.TrainableOpsLength()):
                    self.trainableOps.append(modelTraining.TrainableOps(i))
            else:
                self.trainableOps = modelTraining.TrainableOpsAsNumpy()

    # ModelTrainingT
    def Pack(self, builder):
        if self.optimizerOpt is not None:
            optimizerOpt = self.optimizerOpt.Pack(builder)
        if self.lossfnOpt is not None:
            lossfnOpt = self.lossfnOpt.Pack(builder)
        if self.trainableOps is not None:
            if np is not None and type(self.trainableOps) is np.ndarray:
                trainableOps = builder.CreateNumpyVector(self.trainableOps)
            else:
                ModelTrainingStartTrainableOpsVector(builder, len(self.trainableOps))
                for i in reversed(range(len(self.trainableOps))):
                    builder.PrependInt32(self.trainableOps[i])
                trainableOps = builder.EndVector()
        ModelTrainingStart(builder)
        ModelTrainingAddVersion(builder, self.version)
        ModelTrainingAddOptimizer(builder, self.optimizer)
        ModelTrainingAddOptimizerOptType(builder, self.optimizerOptType)
        if self.optimizerOpt is not None:
            ModelTrainingAddOptimizerOpt(builder, optimizerOpt)
        ModelTrainingAddLossfn(builder, self.lossfn)
        ModelTrainingAddLossfnOptType(builder, self.lossfnOptType)
        if self.lossfnOpt is not None:
            ModelTrainingAddLossfnOpt(builder, lossfnOpt)
        ModelTrainingAddEpochs(builder, self.epochs)
        ModelTrainingAddBatchSize(builder, self.batchSize)
        ModelTrainingAddLossReductionType(builder, self.lossReductionType)
        if self.trainableOps is not None:
            ModelTrainingAddTrainableOps(builder, trainableOps)
        modelTraining = ModelTrainingEnd(builder)
        return modelTraining