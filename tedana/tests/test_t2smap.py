"""
Tests for tedana.
"""
import os.path as op
from shutil import rmtree

import nibabel as nib

from tedana.cli import run_t2smap
from tedana import workflows
from tedana.tests.utils import get_test_data_path


class TestT2smap():
    def test_basic_t2smap1(self):
        """
        A very simple test, to confirm that t2smap creates output
        files.
        """
        data_dir = get_test_data_path()
        label = 't2smap'
        parser = run_t2smap.get_parser()
        options = parser.parse_args(['-d', op.join(data_dir, 'echo1.nii.gz'),
                                     op.join(data_dir, 'echo2.nii.gz'),
                                     op.join(data_dir, 'echo3.nii.gz'),
                                     '-e', '14.5', '38.5', '62.5',
                                     '--combmode', 't2s',
                                     '--fitmode', 'all',
                                     '--label', label])
        workflows.t2smap(**vars(options))
        out_dir = 'TED.echo1.{0}'.format(label)

        # Check outputs
        assert op.isfile(op.join(out_dir, 'ts_OC.nii'))
        img = nib.load(op.join(out_dir, 't2sv.nii'))
        assert len(img.shape) == 3
        img = nib.load(op.join(out_dir, 's0v.nii'))
        assert len(img.shape) == 3
        img = nib.load(op.join(out_dir, 't2svG.nii'))
        assert len(img.shape) == 3
        img = nib.load(op.join(out_dir, 's0vG.nii'))
        assert len(img.shape) == 3
        img = nib.load(op.join(out_dir, 'ts_OC.nii'))
        assert len(img.shape) == 4

    def test_basic_t2smap2(self):
        """
        A very simple test, to confirm that t2smap creates output
        files when fitmode is set to ts.
        """
        data_dir = get_test_data_path()
        label = 't2smap'
        parser = run_t2smap.get_parser()
        options = parser.parse_args(['-d', op.join(data_dir, 'echo1.nii.gz'),
                                     op.join(data_dir, 'echo2.nii.gz'),
                                     op.join(data_dir, 'echo3.nii.gz'),
                                     '-e', '14.5', '38.5', '62.5',
                                     '--combmode', 't2s',
                                     '--fitmode', 'ts',
                                     '--label', label])
        workflows.t2smap(**vars(options))
        out_dir = 'TED.echo1.{0}'.format(label)

        # Check outputs
        assert op.isfile(op.join(out_dir, 'ts_OC.nii'))
        img = nib.load(op.join(out_dir, 't2sv.nii'))
        assert len(img.shape) == 4
        img = nib.load(op.join(out_dir, 's0v.nii'))
        assert len(img.shape) == 4
        img = nib.load(op.join(out_dir, 't2svG.nii'))
        assert len(img.shape) == 4
        img = nib.load(op.join(out_dir, 's0vG.nii'))
        assert len(img.shape) == 4
        img = nib.load(op.join(out_dir, 'ts_OC.nii'))
        assert len(img.shape) == 4

    def test_basic_t2smap3(self):
        """
        A very simple test, to confirm that t2smap creates output
        files when combmode is set to 'ste'.
        """
        data_dir = get_test_data_path()
        label = 't2smap'
        parser = run_t2smap.get_parser()
        options = parser.parse_args(['-d', op.join(data_dir, 'echo1.nii.gz'),
                                     op.join(data_dir, 'echo2.nii.gz'),
                                     op.join(data_dir, 'echo3.nii.gz'),
                                     '-e', '14.5', '38.5', '62.5',
                                     '--combmode', 'ste',
                                     '--fitmode', 'all',
                                     '--label', label])
        workflows.t2smap(**vars(options))
        out_dir = 'TED.echo1.{0}'.format(label)

        # Check outputs
        assert op.isfile(op.join(out_dir, 'ts_OC.nii'))
        img = nib.load(op.join(out_dir, 't2sv.nii'))
        assert len(img.shape) == 3
        img = nib.load(op.join(out_dir, 's0v.nii'))
        assert len(img.shape) == 3
        img = nib.load(op.join(out_dir, 't2svG.nii'))
        assert len(img.shape) == 3
        img = nib.load(op.join(out_dir, 's0vG.nii'))
        assert len(img.shape) == 3
        img = nib.load(op.join(out_dir, 'ts_OC.nii'))
        assert len(img.shape) == 4

    def test_basic_t2smap4(self):
        """
        A very simple test, to confirm that t2smap creates output
        files when combmode is set to 'ste' and fitmode is set to 'ts'.

        Not sure why this fails.
        """
        data_dir = get_test_data_path()
        parser = run_t2smap.get_parser()
        label = 't2smap'
        options = parser.parse_args(['-d', op.join(data_dir, 'echo1.nii.gz'),
                                     op.join(data_dir, 'echo2.nii.gz'),
                                     op.join(data_dir, 'echo3.nii.gz'),
                                     '-e', '14.5', '38.5', '62.5',
                                     '--combmode', 'ste',
                                     '--fitmode', 'ts',
                                     '--label', label])
        workflows.t2smap(**vars(options))
        out_dir = 'TED.echo1.{0}'.format(label)

        # Check outputs
        assert op.isfile(op.join(out_dir, 'ts_OC.nii'))
        img = nib.load(op.join(out_dir, 't2sv.nii'))
        assert len(img.shape) == 4
        img = nib.load(op.join(out_dir, 's0v.nii'))
        assert len(img.shape) == 4
        img = nib.load(op.join(out_dir, 't2svG.nii'))
        assert len(img.shape) == 4
        img = nib.load(op.join(out_dir, 's0vG.nii'))
        assert len(img.shape) == 4
        img = nib.load(op.join(out_dir, 'ts_OC.nii'))
        assert len(img.shape) == 4

    def teardown_method(self):
        # Clean up folders
        rmtree('TED.echo1.t2smap')