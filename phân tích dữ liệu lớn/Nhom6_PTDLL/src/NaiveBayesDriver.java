

import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;
import org.apache.mahout.math.VectorWritable;

public class NaiveBayesDriver extends Configured implements Tool {

	//outut của data
    private final static String CLUSTER_OUTPUT_PATH = "C:\\Users\\Admin\\Desktop\\output_bt\\";
    //file data input raw
    private final static String DATAPATH = "C:\\Users\\Admin\\Desktop\\output_bt\\adult.data";

    //config default của hadoop
    static {
        Configuration.addDefaultResource(("C:\\hadoop-2.7.3\\etc\\hadoop\\hdfs-site.xml"));
        Configuration.addDefaultResource(("C:\\hadoop-2.7.3\\etc\\hadoop\\core-site.xml"));
        Configuration.addDefaultResource(("C:\\hadoop-2.7.3\\etc\\hadoop\\mapred-site.xml"));
    }

    @Override
    public int run(String[] strings) throws Exception {
        Configuration conf = getConf();
        try {
            FileSystem fs = FileSystem.get(conf);
            
            conf.set("in", CLUSTER_OUTPUT_PATH + "discritize/part-r-00000");
            Job job1 = new Job(conf);

            job1.setJarByClass(NaiveBayesDriver.class);

            job1.setMapperClass(PreprocessMapper.class);
            job1.setReducerClass(PreprocessReduce.class);

            job1.setMapOutputKeyClass(Text.class);
            job1.setMapOutputValueClass(DoubleWritable.class);

            job1.setOutputKeyClass(Text.class);
            job1.setOutputValueClass(DoubleWritable.class);
            
            job1.setInputFormatClass(TextInputFormat.class);
            job1.setOutputFormatClass(SequenceFileOutputFormat.class);
            
            TextInputFormat.addInputPath(job1, new Path(DATAPATH));
            SequenceFileOutputFormat.setOutputPath(job1, new Path(CLUSTER_OUTPUT_PATH, "discritize"));
                        
            try {
                job1.waitForCompletion(true);

                Job job2 = new Job(conf);

                job2.setJarByClass(NaiveBayesDriver.class);

                job2.setInputFormatClass(TextInputFormat.class);
                TextInputFormat.addInputPath(job2, new Path(DATAPATH));
                SequenceFileOutputFormat.setOutputPath(job2, new Path(CLUSTER_OUTPUT_PATH, "class"));

                job2.setMapperClass(NaiveBayesMapper.class);
                job2.setReducerClass(NaiveBayesReducer.class);

                job2.setMapOutputKeyClass(Text.class);
                job2.setMapOutputValueClass(IntWritable.class);

                job2.setOutputKeyClass(Text.class);
                job2.setOutputValueClass(DoubleWritable.class);

                job2.waitForCompletion(true);
            } catch (InterruptedException | ClassNotFoundException ex) {
                Logger.getLogger(NaiveBayesDriver.class.getName()).log(Level.SEVERE, null, ex);
            }

        } catch (IOException ex) {
            Logger.getLogger(NaiveBayesDriver.class.getName()).log(Level.SEVERE, null, ex);
        }
        return 0;
    }
}